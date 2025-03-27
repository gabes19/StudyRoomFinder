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
    
    def get_room_data(self,url,capacity):


        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        rooms = []


        for label in soup.find_all('div', class_='panel panel-default'):
            #Extract name of the rooms
            room_name = label.find('h2', class_= 'panel-title').text.strip()
            room_name = room_name.split('\n')[0]
            #Create Room
            room = Room(name = room_name,library = self,capacity = capacity)
            times = label.find_all('div', class_ = 'checkbox')
            #Add all times for room
            for time in times:
                room.available_times.append(time.text.strip())

            rooms.append(room)
            print(room_name)
            

    #Function to scrape times from websites for each library
    #TODO: Collect room description
    def collect_all_times(self):
        #Set up the Chrome driver with headless option
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        driver = webdriver.Chrome(options=options)
        #Open the accessible version of the website (easier for scraping)
        driver.get('https://cal.lib.virginia.edu/r/accessible')


        #Select the library from the dropdown menu
        location_dropdown = Select(driver.find_element(By.ID, 's-lc-location')).select_by_visible_text(self.name)
        #Scrape the available capacities
        capacity_dropdown = Select(driver.find_element(By.ID, 's-lc-type')).options
        #remove 'select the capacity' option
        del capacity_dropdown[0]
        room_capacities = []
        #create text list of capacities to prevent Stale Element Reference
        for i in range(len(capacity_dropdown)):
            room_capacities.append(capacity_dropdown[i].text)

        for capacity in room_capacities:
            #Select capacity
            capacity_dropdown = Select(driver.find_element(By.ID, 's-lc-type')).select_by_visible_text(capacity)
            #Select first option (Either 'Show All' or only one room)
            space_dropdown = Select(driver.find_element(By.ID, 's-lc-space')).select_by_index(0)


            #Show Availability button
            show_availability = driver.find_element(By.ID, 's-lc-go')
            show_availability.click()
            time.sleep(1)


            #Collect room names and available times
            self.rooms = self.get_room_data(driver.current_url, capacity)

            #Go back to form and repopulate library field
            driver.get('https://cal.lib.virginia.edu/r/accessible')
            location_dropdown = Select(driver.find_element(By.ID, 's-lc-location')).select_by_visible_text(self.name)
        return self


def main():
    clark = Library('Brown Science & Engineering Library (Clark Hall)')
    clark.collect_all_times()

#main()






