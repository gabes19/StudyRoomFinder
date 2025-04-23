from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
import os
import time
import requests
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Library, Room, RoomAvailabilitySnapshot, RoomAvailabilityChange, AggregateChanges
from dotenv import load_dotenv
from datetime import datetime,timedelta

#Set up local env -> FOR AWS LAMBDA, environment variable will be configured via their console
BASE_DIR = os.path.abspath(os.path.dirname(__file__)) #Path to app folder
load_dotenv(os.path.join(BASE_DIR, '..', '.env'), override=True) #Load .env (one level up)

DATABASE_URL = os.environ.get("DATABASE_URL")

engine = create_engine(DATABASE_URL, echo=False)
SessionLocal = sessionmaker(bind = engine)
Base.metadata.create_all(engine)


one_minute_ago = datetime.now() - timedelta(minutes=1)

"""
    Helper method to copy and append List[WebelElement]
    to List[String] to prevent stale items.
    Parameters:
        -we_list: List[WebElement] from Selenium Select().options
        -string_list: Existing List[String] to which WebElement text will be appended to
"""

def copy_to_list(we_list, string_list):
    for element in we_list:
        string_list.append(element.text)
    return string_list

"""
    Function to collect all locations from location dropdown.
    Will help populate dropdown in the frontend of the app 
    as well as provide a list of locations for the scraper
"""

def collect_locations():
    session = SessionLocal()
    try:
        #Comment out headless option for local dev
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        driver = webdriver.Chrome(options=options)
        try:
            driver.get("https://cal.lib.virginia.edu/r/accessible")
            location_options = location_dropdown = Select(driver.find_element(By.ID, "s-lc-location")).options
            if location_options[0].text == "Select a Location":
                del location_options[0]
            #copy to string list to prevent Stale Element Reference
            location_list = []
            location_list = copy_to_list(location_options, location_list)
            for location in location_list:
                #Check if library row exists
                existing_lib = (session.query(Library).filter_by(library_name=location).first())
                if not existing_lib:
                    existing_lib = Library(library_name =location, num_rooms =0, rooms = [])
                    session.add(existing_lib)
                    session.commit()
            return location_list    
        finally:
            driver.quit()
    finally:
        session.close()


"""
    Helper function to scrape data availability from url and add to database. 
    Parameters:
        -driver: Selenium Web Driver
        -session: Current SQLALchemy Session
        -Library: Library collecting data for
        -capacity: Capacity of rooms being scraped
"""
def collect_availability(driver: webdriver, session, library: Library, capacity: str, next_day: bool):
    url = driver.current_url
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    collected_rooms = set()
    db_rooms = session.query(Room).filter_by(library_id = library.id, capacity = capacity).all()
    #Each panel label corresponds to a room
    for panel in soup.find_all("div", class_="panel panel-default"):
        #Room data
        room_name_elem = panel.find("h2", class_="panel-title")
        if not room_name_elem:
            continue
        room_name_raw = room_name_elem.text.strip()
        room_name = room_name_raw.split("\n")[0]
        existing_room = session.query(Room).filter_by(room_name = room_name, library_id = library.id).first()
        if not existing_room:
            existing_room = Room(room_name = room_name, capacity = capacity, library_id = library.id)
            session.add(existing_room)
            session.commit()
            library.num_rooms +=1
            session.commit()
        #Room availability snapshots
        time_elements = panel.find_all("div", class_="checkbox")
        available_times = []
        for time_element in time_elements:
            time_text = time_element.text.strip()
            available_times.append(time_text)
        existing_snapshot = session.query(RoomAvailabilitySnapshot).filter(RoomAvailabilitySnapshot.room_id == existing_room.id).filter(
                                                            RoomAvailabilitySnapshot.captured_at >= one_minute_ago).first()
        if not existing_snapshot and not next_day:
            new_snapshot = RoomAvailabilitySnapshot(room_id = existing_room.id, library_id = library.id, captured_at = datetime.now(),
                                                            td_available_times = available_times, td_num_times = len(available_times),
                                                            nd_available_times = [], nd_num_times = 0)
            session.add(new_snapshot)
            session.commit()
            collected_rooms.add(existing_room.id)
        elif existing_snapshot and next_day:
            existing_snapshot.nd_available_times = available_times
            existing_snapshot.nd_num_times = len(available_times)
            session.commit()
            collected_rooms.add(existing_room.id)
    #Add snapshots for existing rooms that weren't found (no times left in the day)
    for room in db_rooms:
        if room.id not in collected_rooms:
            existing_snapshot = session.query(RoomAvailabilitySnapshot).filter(RoomAvailabilitySnapshot.room_id == room.id,
                                        RoomAvailabilitySnapshot.captured_at >= one_minute_ago
                                        ).first()
            if not existing_snapshot and not next_day:
                empty_snapshot = RoomAvailabilitySnapshot(
                room_id=room.id,
                library_id=library.id,
                captured_at=datetime.now(),
                td_available_times=[],
                td_num_times=0,
                nd_available_times=[],
                nd_num_times=0
            )
                session.add(empty_snapshot)
                session.commit()
        elif existing_snapshot and next_day:
            existing_snapshot.nd_available_times = []
            existing_snapshot.nd_num_times = 0
            session.commit()
                
"""
    Function to run scraper and collect data for all libraries.
    -location_list: list[str] of library names
"""

def run_scraper(location_list: list[str]):
    session = SessionLocal()
    try:
        #TODO rework logic
        #Comment out headless option for local dev
        options = webdriver.ChromeOptions()
        #options.add_argument('headless')
        driver = webdriver.Chrome(options=options)
        try:
            for location in location_list:
                library = session.query(Library).filter_by(library_name = location).first()
                #Open the accessible version of the website (easier for scraping)
                driver.get("https://cal.lib.virginia.edu/r/accessible")
                #Select the library from the dropdown menu
                location_dropdown = Select(driver.find_element(By.ID, "s-lc-location")).select_by_visible_text(library.library_name)
                #Scrape the available capacities
                capacity_dropdown = Select(driver.find_element(By.ID, "s-lc-type")).options
                #Remove 'select the capacity' option
                if capacity_dropdown[0].text == "Select the capacity":
                    del capacity_dropdown[0]
                #Create String list to prevent Stale Element Reference
                room_capacities = []
                room_capacities = copy_to_list(capacity_dropdown, room_capacities)
                for capacity in room_capacities:
                    #Select capacity
                    capacity_dropdown = Select(driver.find_element(By.ID, "s-lc-type")).select_by_visible_text(capacity)
                    #Create String list to prevent Stale Element Reference
                    space_dropdown_list = Select(driver.find_element(By.ID, "s-lc-space")).options
                    room_names = []
                    room_names = copy_to_list(space_dropdown_list, room_names)
                    if room_names[0] == "Show All":
                        del room_names[0]
                    for name in room_names:
                        existing_room = session.query(Room).filter_by(room_name = name, library_id = library.id).first()
                        if not existing_room:
                            existing_room = Room(room_name = name, capacity = capacity, library_id = library.id)
                            session.add(existing_room)
                            session.commit()
                            library.num_rooms +=1
                            session.commit()
                    #Select first option (Either 'Show All' or only one room)
                    space_dropdown = Select(driver.find_element(By.ID, "s-lc-space")).select_by_index(0)
                    #Show Availability button
                    show_availability = driver.find_element(By.ID, "s-lc-go")
                    show_availability.click()
                    time.sleep(1)
                    #Collect today's data
                    collect_availability(driver=driver, session=session, library=library, capacity=capacity, next_day=False)
                    #Collect tomorrow's data
                    #Currently assuming second dropdown option is the next day (possible future rework)
                    date_dropdown = Select(driver.find_element(By.ID, "date")).select_by_index(1)
                    show_availability = driver.find_element(By.ID, "s-lc-submit-filters")
                    show_availability.click()
                    collect_availability(driver=driver, session=session, library=library, capacity=capacity, next_day=True)
                    # Go back to form and repopulate library field
                    driver.get("https://cal.lib.virginia.edu/r/accessible")
                    location_dropdown = Select(driver.find_element(By.ID, "s-lc-location")).select_by_visible_text(library.library_name)
        finally:
            driver.quit()
    finally:
        session.close()

"""
    Function to calculate differences between any two room_availability_snapshots.
    Does not add to the database
    Used in collect_recent_availability_changes
"""
#TODO:Ensure filter future times function is working as intended
def calculate_snapshot_difference(prev_snapshot: RoomAvailabilitySnapshot, current_snapshot: RoomAvailabilitySnapshot, session):
    try:
        #Filter out expired time slots
        current_snapshot_time = current_snapshot.captured_at
        def filter_future_times(times,current_snapshot_time):
            future_times = []
            for t in times:
                try:
                    prev_start_str = t.split("-")[0].strip()
                    prev_start_time = datetime.strptime(prev_start_str,"%I:%M%p")
                    if prev_start_time > current_snapshot_time:
                        future_times.append(t)
                except Exception as e:
                    print(f"Error occured in time formatting - {e}")
            return future_times
        td_prev_times = set(filter_future_times(prev_snapshot.td_available_times, current_snapshot_time))
        td_curr_times = set(filter_future_times(current_snapshot.td_available_times, current_snapshot_time))
        #Times that were available but no longer are
        td_reserved = sorted(list(td_prev_times - td_curr_times))
        #Times that were reserved and now are available
        td_released = sorted(list(td_curr_times - td_prev_times))
        td_diff = len(td_curr_times - td_prev_times)
        #Same thing for next day times
        nd_prev_times = set(filter_future_times(prev_snapshot.nd_available_times, current_snapshot_time))
        nd_curr_times = set(filter_future_times(current_snapshot.nd_available_times, current_snapshot_time))
        nd_reserved = sorted(list(nd_prev_times - nd_curr_times))
        nd_released = sorted(list(nd_curr_times - nd_prev_times))
        nd_diff = len(nd_curr_times - nd_prev_times)
        room_availability_change = RoomAvailabilityChange(timestamp = datetime.now(), room_id = current_snapshot.room_id, 
                                    prev_snapshot_id = prev_snapshot.snapshot_id, current_snapshot_id = current_snapshot.snapshot_id,
                                    td_diff = td_diff, nd_diff = nd_diff, td_reserved = td_reserved, td_released = td_released,
                                    nd_reserved = nd_reserved, nd_released = nd_released)
        return room_availability_change
    except Exception as e:
        print(f"Error in calculating snapshot difference - {e}")

"""
    Function to calculate differences between the two most recent snapshots of each room
"""

def collect_recent_availability_changes():
    session = SessionLocal()
    try:
        room_ids = [r[0] for r in session.query(Room.id.distinct()).all()]
        #For every two most recent snapshots of each distinct room id 
        #calculate_snapshot_difference(prev_snapshot, current_snapshot)
        for id in room_ids:
            #Second to last snapshot
            prev_snapshot = (session.query(RoomAvailabilitySnapshot).filter_by(room_id = id)
                             .order_by(RoomAvailabilitySnapshot.captured_at.desc())
                             .offset(1).first())
            #Last snapshot
            current_snapshot = (session.query(RoomAvailabilitySnapshot).filter_by(room_id = id)
                                .order_by(RoomAvailabilitySnapshot.captured_at.desc())
                                .first())
            if prev_snapshot:
                availability_change = calculate_snapshot_difference(prev_snapshot = prev_snapshot, current_snapshot = current_snapshot, session = session)
                session.add(availability_change)
                session.commit()
    finally:
        session.close()

"""
    Function to aggregate most recent availability changes from Room level -> Library Level
    -location_list: List[str] of library names
"""

def aggregate_availability_changes(location_list: list[str]):
    session = SessionLocal()
    try:
        for location in location_list:
            library = session.query(Library).filter_by(library_name = location).first()
            #Query list of room ids belonging to the library
            room_ids = [r[0] for r in session.query(Room.id.distinct()).filter_by(library_id = library.id).all()]
            #Query most recent availability change calculation for each room, filtering in only room_ids from the list
            availability_changes = (session.query(RoomAvailabilityChange).filter(RoomAvailabilityChange.room_id.in_(room_ids))
                                    .order_by(RoomAvailabilityChange.timestamp.desc()).limit(1).all())
            agg_td_diff = 0
            agg_nd_diff = 0
            td_num_reserved = 0
            td_num_released = 0
            nd_num_reserved = 0
            nd_num_released = 0
            for ac in availability_changes:
                agg_td_diff += ac.td_diff
                agg_nd_diff += ac.nd_diff
                td_num_reserved += len(ac.td_reserved) 
                td_num_released += len(ac.td_released)
                nd_num_reserved += len(ac.nd_reserved) 
                nd_num_released += len(ac.nd_released)
            aggregate_changes = (AggregateChanges(library_id = library.id, timestamp = datetime.now(), agg_td_diff = agg_td_diff, 
                                                agg_nd_diff = agg_nd_diff, td_num_reserved = td_num_reserved, td_num_released = td_num_released,
                                                nd_num_reserved = nd_num_reserved, nd_num_released = nd_num_released))
            session.add(aggregate_changes)
            session.commit()
    finally:
        session.close()



def main():
    locations = collect_locations()
    run_scraper(locations)
    collect_recent_availability_changes()
    aggregate_availability_changes(locations)
main()