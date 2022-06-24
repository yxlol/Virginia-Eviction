## Import Selenium Library (needs installation, refer to https://www.selenium.dev/documentation/webdriver/) and Firefox webdriver. 
## Editor's Draft is here: https://w3c.github.io/webdriver/#is-element-selected 
import random 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from Date_Generator import Date_Generator
from Data_Construction import Data_Construction

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

## element paths

x_path_select_court = '/html/body/table[1]/tbody/tr[1]/td/table/tbody/tr[2]/td[1]/div/table/tbody/tr/td/div[2]/div[1]/div/table/tbody/tr[1]/td/table/tbody/tr/td[2]/img'
court_name = '/html/body/ul/li[131]/a'
url_landing = 'https://eapps.courts.state.va.us/gdcourts/landing.do?landing=landing'
x_path_agree = '/html/body/table/tbody/tr[1]/td/table/tbody/tr[3]/td/form/table/tbody/tr[2]/td/input[1]'
x_path_search_tab = '/html/body/table[1]/tbody/tr[1]/td/table/tbody/tr[2]/td[1]/div/table/tbody/tr/td/div[2]/div[3]/div/ul/li[3]/span/a'
x_path_hearing_date = '/html/body/table[1]/tbody/tr[1]/td/table/tbody/tr[2]/td[2]/form/table/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr[1]/td[2]/input'
x_path_1 = '/html/body/table[1]/tbody/tr[1]/td/table/tbody/tr[2]/td[2]/form/table/tbody/tr[2]/td/span/input'
x_path_2 = '/html/body/table[1]/tbody/tr[1]/td/table/tbody/tr[2]/td[2]/form/table/tbody/tr[2]/td/span/input[2]'

UD = Data_Construction()

def date_keys(day, month, year, delta):
    date = Date_Generator()
    return date.date_input(day, month, year, delta)
date_list = date_keys(1,8,2019,30)
print(date_list)

def search_UD(i):
    condition = True
    driver = webdriver.Chrome()
    driver.get("https://eapps.courts.state.va.us/gdcourts/welcomePage.do?") 
    time.sleep(random.randint(0,2))
    driver.find_element(by=By.XPATH, value=x_path_select_court).click()
    time.sleep(random.randint(0,2))
    driver.find_element(by=By.XPATH, value=court_name).click()
    time.sleep(1)
    driver.find_element(by=By.XPATH, value=x_path_search_tab).click()
    time.sleep(random.randint(0,2))

    element = driver.find_element(by=By.ID, value="txthearingdate")
    element.clear()
    try:
        element.send_keys(date_list[i] + Keys.ENTER).perform() # Enter target date
    except AttributeError: 
       while condition:
           WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "tableborder")))
           source = driver.find_element(by=By.CLASS_NAME, value="tableborder")
           content = source.get_attribute("outerHTML")
           p = HTMLTableParser()
           p.feed(content)
           raw_data = p.tables
           time.sleep(2)
           if "Unlawful Detainer" in driver.page_source:
                   UD.clean_data(raw_data,date_list[i])
           if "caseInfoScrollForward" not in driver.page_source:
               condition = False
               driver.quit()
           elif "caseInfoScrollForward"in driver.page_source and "caseInfoScrollBack" in driver.page_source:
               driver.find_element(By.XPATH, x_path_2).click()
               
           else:
               driver.find_element(By.XPATH, x_path_1).click() 

def recursive_scrape():
    for i in range(0, len(date_list)):
        search_UD(i)
    print(UD.dataframe())
    if UD.dataframe() is not None:
        UD.to_csv()

recursive_scrape()
    
