## Import Selenium Library (needs installation, refer to https://www.selenium.dev/documentation/webdriver/) and Firefox webdriver. 
## Editor's Draft is here: https://w3c.github.io/webdriver/#is-element-selected 
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from Date_Generator import Date_Generator 



driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

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
# Needs modification... date_str = 
driver.find_element(by=By.XPATH, value=xpath).click()
driver.implicitly_wait(3)
driver.find_element(by=By.XPATH, value=xpath_w).click()
driver.implicitly_wait(4)
driver.find_element(by=By.XPATH, value=xpath_submit).click()
driver.implicitly_wait(4)
SearchInput = driver.find_element(by = By.XPATH, value=xpath_date_box)
#SearchInput.click().click().click() -- triple click does not work.
#SearchInput.clear()
#SearchInput.send_keys(date_str + Keys.ENTER)

## Take action on element

## Request element information 


## Close the browser
