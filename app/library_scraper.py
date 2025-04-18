from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
import os
import time
import requests
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Library, Room, RoomAvailabilitySnapshot
from dotenv import load_dotenv
from datetime import datetime,timedelta

#Set up local env -> FOR AWS LAMBDA, environment variable will be configured via their console
BASE_DIR = os.path.abspath(os.path.dirname(__file__)) #Path to app folder
load_dotenv(os.path.join(BASE_DIR, '..', '.env'), override=True) #Load .env (one level up)

DATABASE_URL = os.environ.get("DATABASE_URL")

engine = create_engine(DATABASE_URL, echo=True)
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
    Function to run scraper and collect data for all libraries.
"""

def run_scraper(library_name: str):
    #Initiate db session
    session = SessionLocal()
    
    try:
        #Check if library row exists
        existing_lib = (session.query(Library).filter_by(library_name=library_name).first())
        if not existing_lib:
            existing_lib = Library(library_name =library_name, num_rooms =0, rooms = [])
            session.add(existing_lib)
            session.commit()
        # Set up the Chrome driver with headless option
        options = webdriver.ChromeOptions()
        #options.add_argument('headless')
        driver = webdriver.Chrome(options=options)
        try:
            # Open the accessible version of the website (easier for scraping)
            driver.get("https://cal.lib.virginia.edu/r/accessible")
            # Select the library from the dropdown menu
            location_dropdown = Select(driver.find_element(By.ID, "s-lc-location")).select_by_visible_text(library_name)
            # Scrape the available capacities
            capacity_dropdown = Select(driver.find_element(By.ID, "s-lc-type")).options
            # Remove 'select the capacity' option
            if capacity_dropdown[0] == "Select the capacity":
                del capacity_dropdown[0]
            # Create String list to prevent Stale Element Reference
            room_capacities = []
            room_capacities = copy_to_list(capacity_dropdown, room_capacities)
            for capacity in room_capacities:
                # Select capacity
                capacity_dropdown = Select(driver.find_element(By.ID, "s-lc-type")).select_by_visible_text(capacity)
                # Create String list to prevent Stale Element Reference
                space_dropdown_list = Select(driver.find_element(By.ID, "s-lc-space")).options
                room_names = []
                room_names = copy_to_list(space_dropdown_list, room_names)
                if room_names[0] == "Show All":
                    del room_names[0]
                for name in room_names:
                    existing_room = session.query(Room).filter_by(room_name = name, library_id = existing_lib.id).first()
                    if not existing_room:
                        existing_room = Room(room_name = name, capacity = capacity, library_id = existing_lib.id)
                        session.add(existing_room)
                        session.commit()
                        existing_lib.num_rooms +=1
                        session.commit()
                # Select first option (Either 'Show All' or only one room)
                space_dropdown = Select(driver.find_element(By.ID, "s-lc-space")).select_by_index(0)
                # Show Availability button
                show_availability = driver.find_element(By.ID, "s-lc-go")
                show_availability.click()
                time.sleep(1)
                url = driver.current_url
                response = requests.get(url)
                soup = BeautifulSoup(response.content, "html.parser")
                #Each panel label corresponds to a room
                for panel in soup.find_all("div", class_="panel panel-default"):
                    # #Room data
                    # room_name_elem = panel.find("h2", class_="panel-title")
                    # if not room_name_elem:
                    #     continue
                    # room_name_raw = room_name_elem.text.strip()
                    # room_name = room_name_raw.split("\n")[0]
                    # existing_room = session.query(Room).filter_by(room_name = room_name, library_id = existing_lib.id).first()
                    # if not existing_room:
                    #     existing_room = Room(room_name = room_name, capacity = capacity, library_id = existing_lib.id)
                    #     session.add(existing_room)
                    #     session.commit()
                    #     existing_lib.num_rooms +=1
                    #     session.commit()
                        #Room availability snapshots
                        time_elements = panel.find_all("div", class_="checkbox")
                        available_times = []
                        for time_element in time_elements:
                            time_text = time_element.text.strip()
                            available_times.append(time_text)
                        existing_snapshot = session.query(RoomAvailabilitySnapshot).filter(RoomAvailabilitySnapshot.room_id == existing_room.id).filter(
                            RoomAvailabilitySnapshot.captured_at >= one_minute_ago).first()
                        if not existing_snapshot:
                            #TODO: add scraping for next day
                            new_snapshot = RoomAvailabilitySnapshot(room_id = existing_room.id, library_id = existing_lib.id, captured_at = datetime.now(),
                                                                          td_available_times = available_times, td_num_times = len(available_times),
                                                                            nd_available_times = [], nd_num_times = 0)
                            session.add(new_snapshot)
                            session.commit()
                # Go back to form and repopulate library field
                driver.get("https://cal.lib.virginia.edu/r/accessible")
                location_dropdown = Select(driver.find_element(By.ID, "s-lc-location")).select_by_visible_text(library_name)
        finally:
            driver.quit()
    finally:
        session.close()

def main():
    run_scraper("Shannon Library")
main()