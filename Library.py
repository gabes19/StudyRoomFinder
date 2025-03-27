from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import pandas as pd
from bs4 import BeautifulSoup
import time, requests
import Room
class Library:
    def __init__(self,name):
        self.name = name
        self.rooms = []  #List of StudyRoom objects in the library 
    
    def get_room_data(url):
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        times = []
        for label in soup.find_all('panel panel-default'):
            #Extract name of the rooms
            #extracts and strips whitespace
            time_slot = label.get_text(strip=True)
            #only take in time labels
            if time_slot[0].isdigit():
                times.append(time_slot)
        return times
    #Function to scrape times from websites for each library
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
        room_capacities = Select(driver.find_element(By.ID, 's-lc-type')).options
        for capacity in room_capacities:
            capacity_dropdown = Select(driver.find_element(By.ID, 's-lc-type')).select_by_visible_text(capacity.text)
            #Select first option (Either 'Show All' or only one room)
            space_dropdown = Select(driver.find_element(By.ID, 's-lc-space')).select_by_index(0)
            #Show Availability button
            show_availability = driver.find_element(By.ID, 's-lc-go')
            show_availability.click()
            time.sleep(1)
            #Collect room name and available times
            self.get_room_data(driver.current_url)








