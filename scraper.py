import random 
import logging 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC


from html_table_parser.parser import HTMLTableParser

# pretty-print python data structures
from pprint import pprint

# for parsing all the tables present
# on the website
from html_table_parser.parser import HTMLTableParser

# for converting the parsed data in a
# pandas dataframe
import pandas as pd

import time

import os

from Case_Details import Case_Details

CD = Case_Details()

x_path_case_number = '/html/body/table[1]/tbody/tr[1]/td/table/tbody/tr[2]/td[1]/div/table/tbody/tr/td/div[2]/div[3]/div/ul/li[2]/span/a'
x_path_number_input = '/html/body/table[1]/tbody/tr[1]/td/table/tbody/tr[2]/td[2]/form/table/tbody/tr[2]/td/table/tbody/tr[1]/td[2]/input'
x_path_select_court = '/html/body/table[1]/tbody/tr[1]/td/table/tbody/tr[2]/td[1]/div/table/tbody/tr/td/div[2]/div[1]/div/table/tbody/tr[1]/td/table/tbody/tr/td[2]/img'
x_path_table = '/html/body/table[1]/tbody/tr[1]/td/table/tbody/tr[2]/td[2]/form/div/table'
court_name = '/html/body/ul/li[131]/a' # Williamsburg/James City County Court
case_list = [] 
case_list = pd.read_excel('220725.xlsx').iloc[:,1].drop_duplicates().tolist()
print(len(case_list))

driver = webdriver.Chrome()
driver.get("https://eapps.courts.state.va.us/gdcourts/welcomePage.do?") # Get on the general district court website
driver.find_element(by=By.XPATH, value=x_path_select_court).click() # Select Williamsburg/James City County Court 
time.sleep(random.randint(0,2))
driver.find_element(by=By.XPATH, value=court_name).click() # Modify the variable above to go to a different court 
time.sleep(2)
for i in range(len(case_list)):
    driver.find_element(by=By.XPATH, value=x_path_case_number).click() # Search by Case Number
    driver.find_element(by=By.XPATH, value=x_path_number_input).click() # Input Case Number
    time.sleep(random.randint(0,2))
    element = driver.find_element(by=By.ID, value="displayCaseNumber")
    try:
        element.send_keys(case_list[i] + Keys.ENTER).perform()
    except AttributeError: # I can't get rid of the error, but I have to use .perform()
        time.sleep(random.randint(0,4))
        table = driver.find_element(by=By.XPATH, value = x_path_table) # Scrape the entire table
        table_value = table.get_attribute("outerHTML") 
        p = HTMLTableParser() # The parser I use (the result would be in list format with .tables)
        p.feed(table_value)
        full_table = p.tables
        try:
            CD.clean_table(full_table) # Use Case_Details.py to clean the table 
        except IndexError:
            print(str(case_list[i]), 'is not scrapable')

        time.sleep(random.randint(0,3))
CD.data_frame() # Construct a Data Frame
CD.to_excel() # Convert to excel


