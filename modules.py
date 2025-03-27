from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import pandas as pd
from bs4 import BeautifulSoup
import time, requests
from Library import Library
from Room import StudyRoom

    
def get_time_slots(url):
  response = requests.get(url)
  soup = BeautifulSoup(response.content, 'html.parser')
  times = []
  for label in soup.find_all('label'):
      #extracts and strips whitespace
      time_slot = label.get_text(strip=True)
      #only take in time labels
      if time_slot[0].isdigit():
        times.append(time_slot)
  return times

def collect_clark():
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    driver = webdriver.Chrome(options=options)
    #Accessible page for scraping
    driver.get('https://cal.lib.virginia.edu/r/accessible')


    #Create Clark Library object
    clark = Library('Brown Science & Engineering Library (Clark Hall)')

    #Capacity dict stores study room capacities as keys and form values as values
    capacities = {'Space For 1-4 People': 1,'Space For 5-8 People': 2,'Space For 9-12 People' : 3,'Space For 13+ People' : 4}

    #Iterate through available capacities (each capacity has a list of rooms)
    for capacity in capacities:
        value = capacities.get(capacity)
        #select Clark library
        location_dropdown = Select(driver.find_element(By.ID, 's-lc-location')).select_by_visible_text('Brown Science & Engineering Library (Clark Hall)')

        #Select capacity dropdown and choose option for current capacity
        capacity_dropdown = Select(driver.find_element(By.ID, 's-lc-type')).select_by_value(str(value))

        #Select room dropdown, do not choose option yet
        space_dropdown = Select(driver.find_element(By.ID, 's-lc-space'))
        for i in range(len(space_dropdown.options)):
            room = space_dropdown.options[i]
            room_text = room.text
            if room_text != "Show All":
                #Create new Clark StudyRoom Object
                new_room = StudyRoom(name = room.text,library=clark)
                clark.rooms.append(new_room)
                clark.num_rooms+=1

                #Select current StudyRoom as option
                select_room = space_dropdown.select_by_visible_text(room.text)

                #Show Availability button
                show_availability = driver.find_element(By.ID, 's-lc-go')
                show_availability.click()
                time.sleep(1)

                #Set StudyRoom attributes
                new_room.url = driver.current_url
                new_room.available_times = get_time_slots(new_room.url)
                new_room.num_times = len(new_room.available_times)
                new_room.capacity = capacity
                #Return to form page
                driver.get('https://cal.lib.virginia.edu/r/accessible')

                #repopulate
                location_dropdown = Select(driver.find_element(By.ID, 's-lc-location')).select_by_visible_text('Brown Science & Engineering Library (Clark Hall)')
                capacity_dropdown = Select(driver.find_element(By.ID, 's-lc-type')).select_by_value(str(value))
                space_dropdown = Select(driver.find_element(By.ID, 's-lc-space'))
    return clark
#TODO
def collect_clem():
    return
#TODO
def collect_rmc():
    return

def collect_shannon():
    driver = webdriver.Chrome()
    #Accessible page for scraping
    driver.get('https://cal.lib.virginia.edu/r/accessible')


    #Create Library object
    shannon = Library('Shannon Library')

    #Capacity dict stores study room capacities as keys and form values as values
    capacities = {'Space For 5-8 People': 2,'Space For 13+ People' : 4}

    #Iterate through available capacities (each capacity has a list of rooms)
    for capacity in capacities:
        value = capacities.get(capacity)
        #select library
        location_dropdown = Select(driver.find_element(By.ID, 's-lc-location')).select_by_visible_text('Shannon Library')

        #Select capacity dropdown and choose option for current capacity
        capacity_dropdown = Select(driver.find_element(By.ID, 's-lc-type')).select_by_value(str(value))

        #Select room dropdown, do not choose option yet
        space_dropdown = Select(driver.find_element(By.ID, 's-lc-space'))
        for i in range(len(space_dropdown.options)):
            room = space_dropdown.options[i]
            room_text = room.text
            if room_text != "Show All":
                #Create new StudyRoom Object
                new_room = StudyRoom(name = room.text,library=shannon)
                shannon.rooms.append(new_room)
                shannon.num_rooms+=1

                #Select current StudyRoom as option
                select_room = space_dropdown.select_by_visible_text(room.text)

                #Show Availability button
                show_availability = driver.find_element(By.ID, 's-lc-go')
                show_availability.click()
                time.sleep(1)

                #Set StudyRoom attributes
                new_room.url = driver.current_url
                new_room.available_times = get_time_slots(new_room.url)
                new_room.num_times = len(new_room.available_times)
                new_room.capacity = capacity
                #Return to form page
                driver.get('https://cal.lib.virginia.edu/r/accessible')

                #repopulate
                location_dropdown = Select(driver.find_element(By.ID, 's-lc-location')).select_by_visible_text('Shannon Library')
                capacity_dropdown = Select(driver.find_element(By.ID, 's-lc-type')).select_by_value(str(value))
                space_dropdown = Select(driver.find_element(By.ID, 's-lc-space'))

def collect_music():
    driver = webdriver.Chrome()
    #Accessible page for scraping
    driver.get('https://cal.lib.virginia.edu/r/accessible')


    #Create Library object
    music = Library('Music Library')

    #Capacity dict stores study room capacities as keys and form values as values
    capacities = {'Space For 1-4 People' : 1, 'Space For 9-12 People': 3}

    #Iterate through available capacities (each capacity has a list of rooms)
    for capacity in capacities:
        value = capacities.get(capacity)
        #select library
        location_dropdown = Select(driver.find_element(By.ID, 's-lc-location')).select_by_visible_text('Music Library')

        #Select capacity dropdown and choose option for current capacity
        capacity_dropdown = Select(driver.find_element(By.ID, 's-lc-type')).select_by_value(str(value))

        #Select room dropdown, do not choose option yet
        space_dropdown = Select(driver.find_element(By.ID, 's-lc-space'))
        for i in range(len(space_dropdown.options)):
            room = space_dropdown.options[i]
            room_text = room.text
            if room_text != "Show All":
                #Create new StudyRoom Object
                new_room = StudyRoom(name = room.text,library=music)
                music.rooms.append(new_room)
                music.num_rooms+=1

                #Select current StudyRoom as option
                select_room = space_dropdown.select_by_visible_text(room.text)

                #Show Availability button
                show_availability = driver.find_element(By.ID, 's-lc-go')
                show_availability.click()
                time.sleep(1)

                #Set StudyRoom attributes
                new_room.url = driver.current_url
                new_room.available_times = get_time_slots(new_room.url)
                new_room.num_times = len(new_room.available_times)
                new_room.capacity = capacity
                #Return to form page
                driver.get('https://cal.lib.virginia.edu/r/accessible')

                #repopulate
                location_dropdown = Select(driver.find_element(By.ID, 's-lc-location')).select_by_visible_text('Music Library')
                capacity_dropdown = Select(driver.find_element(By.ID, 's-lc-type')).select_by_value(str(value))
                space_dropdown = Select(driver.find_element(By.ID, 's-lc-space'))

def collect_finearts():
    driver = webdriver.Chrome()
    #Accessible page for scraping
    driver.get('https://cal.lib.virginia.edu/r/accessible')


    #Create Library object
    fine_arts = Library('Fine Arts Library')

    #Capacity dict stores study room capacities as keys and form values as values
    capacities = {'Space For 5-8 People' : 2}

    #Iterate through available capacities (each capacity has a list of rooms)
    for capacity in capacities:
        value = capacities.get(capacity)
        #select library
        location_dropdown = Select(driver.find_element(By.ID, 's-lc-location')).select_by_visible_text('Fine Arts Library')

        #Select capacity dropdown and choose option for current capacity
        capacity_dropdown = Select(driver.find_element(By.ID, 's-lc-type')).select_by_value(str(value))

        #Select room dropdown, do not choose option yet
        space_dropdown = Select(driver.find_element(By.ID, 's-lc-space'))
        for i in range(len(space_dropdown.options)):
            room = space_dropdown.options[i]
            room_text = room.text
            if room_text != "Show All":
                #Create new StudyRoom Object
                new_room = StudyRoom(name = room.text,library=fine_arts)
                fine_arts.rooms.append(new_room)
                fine_arts.num_rooms+=1

                #Select current StudyRoom as option
                select_room = space_dropdown.select_by_visible_text(room.text)

                #Show Availability button
                show_availability = driver.find_element(By.ID, 's-lc-go')
                show_availability.click()
                time.sleep(1)

                #Set StudyRoom attributes
                new_room.url = driver.current_url
                new_room.available_times = get_time_slots(new_room.url)
                new_room.num_times = len(new_room.available_times)
                new_room.capacity = capacity
                #Return to form page
                driver.get('https://cal.lib.virginia.edu/r/accessible')

                #repopulate
                location_dropdown = Select(driver.find_element(By.ID, 's-lc-location')).select_by_visible_text('Fine Arts Library')
                capacity_dropdown = Select(driver.find_element(By.ID, 's-lc-type')).select_by_value(str(value))
                space_dropdown = Select(driver.find_element(By.ID, 's-lc-space'))