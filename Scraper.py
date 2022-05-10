## Import Selenium Library (needs installation, refer to https://www.selenium.dev/documentation/webdriver/) and Firefox webdriver. 
## Editor's Draft is here: https://w3c.github.io/webdriver/#is-element-selected 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from Date_Generator import Date_Generator
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# from webdriver_manager.firefox import GeckoDriverManager

## Start the session.
## This is the database that covers the majority of Circuit Courts information in Virginia, besides Circuit Courts of Alexandria and Fairfax.
driver.get("http://ewsocis1.courts.state.va.us/CJISWeb/circuit.jsp") 

## Take actions 

## Request information 

## Waiting Strategies: https://www.selenium.dev/documentation/webdriver/waits/

## Find element

xpath = '//*[@id="BackgroundWhite"]/table/tbody/tr[2]/td/table[1]/tbody/tr[1]/td[1]'
xpath_w = '//*[@id="BackgroundWhite"]/table/tbody/tr[2]/td/table[1]/tbody/tr[1]/td[1]/select/option[116]'
xpath_submit = '//*[@id="courtSubmit"]'
xpath_date_box = '//*[@id="BackgroundWhite"]/td/table[2]/tbody/tr/td/table[2]/tbody/tr/td[2]'
date = Date_Generator()
date.date_input(1,1,2022,0)
# Needs modification... date_str = 
xpath_civil = '//*[@id="fontBoldExample"]/input[2]'
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
driver.find_element(by = By.XPATH, value = xpath_date_box).send_keys("01012022" + Keys.ENTER).perform()
#for i in date.date_input(1,1,2022,0):
#SearchInput.send_keys(date_str + Keys.ENTER)

## Take action on element

## Request element information 


## Close the browser
