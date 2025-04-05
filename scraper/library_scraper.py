#TODO: Refactor this class into a library scraper(shifting to a database model)

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import pandas as pd
from bs4 import BeautifulSoup
import time, requests
from Room import Room
class Library:
    def __init__(self,name):
        self.name = name #String name of the Library
        self.rooms = []  #List of Room objects in the library 

    '''
        Function to collect all timeslots available for rooms at a specific capacity
        Parameters:
            -url: url of page containing room data
            -capacity: String capacity of rooms to collect data for (taken from capacity dropdown)
            -room_names: List[String] room names at this library (taken from space dropdown)
    '''
    def get_room_data(self,url,capacity,room_names):
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        #Create a room object for every room
        rooms = []
        for name in room_names:
            room = Room(name = name, library = self, capacity = capacity)
            rooms.append(room)
        #Each panel label corresponds to a room
        for label in soup.find_all('div', class_='panel panel-default'):
            #Collect room name
            room_name = label.find('h2', class_= 'panel-title').text.strip()
            room_name = room_name.split('\n')[0]
            #Match room name in panel to room_name list and include available times
            if room_name in room_names:
                for room_object in rooms:
                    if room_object.name == room_name:
                        times = label.find_all('div', class_ = 'checkbox')
                        #Add all times for room
                        for time in times:
                            room.available_times.append(time.text.strip())
        return rooms
            
    '''
        Helper function to copy and append List[WebelElement]
        to List[String] to prevent stale items.
        Parameters:
            -we_list: List[WebElement] from Selenium Select().options
            -string_list: Existing List[String] to which WebElement text will be appended to
    '''
    @staticmethod
    def copy_to_list(we_list,string_list):
        for i in range(len(we_list)):
            string_list.append(we_list[i].text)
        return string_list
    
    '''
        Function called to collect a Library's rooms and available timeslots
    '''
    #TODO: Implement boolean parameter next_day to collect times from next day
    def collect_all_times(self):
        #Set up the Chrome driver with headless option
        options = webdriver.ChromeOptions()
        #options.add_argument('headless')
        driver = webdriver.Chrome(options=options)
        #Open the accessible version of the website (easier for scraping)
        driver.get('https://cal.lib.virginia.edu/r/accessible')
        #Select the library from the dropdown menu
        location_dropdown = Select(driver.find_element(By.ID, 's-lc-location')).select_by_visible_text(self.name)
        #Scrape the available capacities
        capacity_dropdown = Select(driver.find_element(By.ID, 's-lc-type')).options
        #Remove 'select the capacity' option
        if capacity_dropdown[0] == 'Select the capacity':
            del capacity_dropdown[0]
        #Create String list to prevent Stale Element Reference
        room_capacities = []
        room_capacities = self.copy_to_list(capacity_dropdown, room_capacities)
        room_names = []
        for capacity in room_capacities:
            #Select capacity
            capacity_dropdown = Select(driver.find_element(By.ID, 's-lc-type')).select_by_visible_text(capacity)
            #Create String list to prevent Stale Element Reference
            space_dropdown_list = Select(driver.find_element(By.ID,'s-lc-space')).options
            room_names = []
            room_names = self.copy_to_list(space_dropdown_list, room_names)
            if room_names[0] == "Show All":
                del room_names[0]
            #Select first option (Either 'Show All' or only one room)
            space_dropdown = Select(driver.find_element(By.ID, 's-lc-space')).select_by_index(0)
            #Show Availability button
            show_availability = driver.find_element(By.ID, 's-lc-go')
            show_availability.click()
            time.sleep(1)
            #Collect room names and available times
            rooms_at_this_capacity = self.get_room_data(driver.current_url, capacity, room_names)
            for room in rooms_at_this_capacity:
                self.rooms.append(room)
            #Go back to form and repopulate library field
            driver.get('https://cal.lib.virginia.edu/r/accessible')
            location_dropdown = Select(driver.find_element(By.ID, 's-lc-location')).select_by_visible_text(self.name)
        return self


def main():
    lib = Library("Shannon Library")
    lib.collect_all_times()
    for room in lib.rooms: 
        print(room.name)
        print(room.available_times)
main()






