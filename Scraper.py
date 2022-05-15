## Import Selenium Library (needs installation, refer to https://www.selenium.dev/documentation/webdriver/) and Firefox webdriver. 
## Editor's Draft is here: https://w3c.github.io/webdriver/#is-element-selected 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
#from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from Date_Generator import Date_Generator


# Library for opening url and creating
# requests
import urllib.request

# pretty-print python data structures
from pprint import pprint

# for parsing all the tables present
# on the website
from html_table_parser.parser import HTMLTableParser

# for converting the parsed data in a
# pandas dataframe
import pandas as pd

import csv, os

#driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

## Start the session.
## This is the database that covers the majority of Circuit Courts information in Virginia, besides Circuit Courts of Alexandria and Fairfax.
#driver.get("http://ewsocis1.courts.state.va.us/CJISWeb/circuit.jsp") 

## Take actions 

## Request information 

## Waiting Strategies: https://www.selenium.dev/documentation/webdriver/waits/

## Find element

xpath = '//*[@id="BackgroundWhite"]/table/tbody/tr[2]/td/table[1]/tbody/tr[1]/td[1]'
xpath_w = '//*[@id="BackgroundWhite"]/table/tbody/tr[2]/td/table[1]/tbody/tr[1]/td[1]/select/option[116]'
xpath_submit = '//*[@id="courtSubmit"]'
xpath_date_box = '/html/body/table/tbody/tr/td/table/tbody/tr[3]/td/table[2]/tbody/tr/td/table[2]/tbody/tr/td[2]/input[2]'

# Needs modification... date_str = 
xpath_civil = '//*[@id="fontBoldExample"]/input[2]'

def date_keys(day, month, year, delta):
    date = Date_Generator()
    return date.date_input(day, month, year, delta)

date_list = date_keys(1,1,2019,5)


for i in date_list:
    if i is None:
        pass
    else:
        driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        driver.get("http://ewsocis1.courts.state.va.us/CJISWeb/circuit.jsp") 
        driver.find_element(by=By.XPATH, value=xpath).click()
        driver.implicitly_wait(8)
        driver.find_element(by=By.XPATH, value=xpath_w).click()
        driver.implicitly_wait(10)
        driver.find_element(by=By.XPATH, value=xpath_submit).click()
        driver.implicitly_wait(10)
        driver.find_element(by=By.XPATH, value=xpath_civil).click()
        SearchInput = driver.find_element(by = By.XPATH, value=xpath_date_box)
        element = driver.find_element(by = By.ID, value = "selectCheck")
        element.clear()
        driver.find_element(by = By.XPATH, value = xpath_date_box).send_keys(i + Keys.ENTER).perform()
    driver.quit()
#for i in date.date_input(1,1,2022,0):
#SearchInput.send_keys(date_str + Keys.ENTER)

## Take action on element

## Request element information 


## Close the browser
