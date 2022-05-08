from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
## Import Selenium Library (needs installation, refer to https://www.selenium.dev/documentation/webdriver/) and Firefox webdriver. 

driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
driver.get("http://ewsocis1.courts.state.va.us/CJISWeb/circuit.jsp") 
## This is the database that covers the majority of Circuit Courts information in Virginia, besides Circuit Courts of Alexandria and Fairfax.