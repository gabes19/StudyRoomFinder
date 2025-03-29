from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import pandas as pd
from bs4 import BeautifulSoup
import time, requests
from Room import Room
class Library:
    def __init__(self,name):
        self.name = name
        self.rooms = []  #List of StudyRoom objects in the library 
    #TODO: Test this: Rework this logic to match room_names and times
    def get_room_data(self,url,capacity,room_names):


        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        rooms = []
        for name in room_names:
            room = Room(name = name, library = self, capacity = capacity)
            rooms.append(room)
        

        for label in soup.find_all('div', class_='panel panel-default'):
            #Match room names and include available times
            room_name = label.find('h2', class_= 'panel-title').text.strip()
            room_name = room_name.split('\n')[0]
            if room_name in room_names:
                for room_object in rooms:
                    if room_object.name == room_name:
                        times = label.find_all('div', class_ = 'checkbox')
                        #Add all times for room
                        for time in times:
                            room.available_times.append(time.text.strip())
            #debugging print
            print(room_name)
        return rooms
            
    #helper function to copy and append List[Webelements] to List[String] to prevent stale items
    @staticmethod
    def copy_to_list(we_list,string_list):
        for i in range(len(we_list)):
            string_list.append(we_list[i].text)
        return string_list
    #Function to scrape times from websites for each library
    #TODO: Collect room description
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
        #remove 'select the capacity' option
        if capacity_dropdown[0] == 'Select the capacity':
            del capacity_dropdown[0]
        #create String list to prevent Stale Element Reference
        room_capacities = []
        room_capacities = self.copy_to_list(capacity_dropdown, room_capacities)
        

        
        room_names = []
        for capacity in room_capacities:
            #Select capacity
            capacity_dropdown = Select(driver.find_element(By.ID, 's-lc-type')).select_by_visible_text(capacity)
            space_dropdown_list = Select(driver.find_element(By.ID,'s-lc-space')).options
            #Create String list to prevent Stale Element Reference
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






