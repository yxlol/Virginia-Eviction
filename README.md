# Eviction Case Data Scraping Project

## Introduction 
This project is part of a research sponsored by Charles Center at College of William and Mary in Virginia, United States. Our plan is to create a open-source database of eviction data in Williamsburg and James City County. This involves web scraping from online docket (http://ewsocis1.courts.state.va.us/CJISWeb/circuit.jsp) and manually gather information from the court. A more detailed and accurate methodology would be updated later.

While we are still working on finding the right tools and writing the scripts, I would welcome any insights in the project. Feel free to contact me on matrix lolitsme:matrix.org or mastodon y_x at mastodon.social  for any questions/comments.You can also email me at: yxiao03@wm.edu. Still a newbie in web scraping, and any advice would be appreciated. If you want to make any contributions, please use pull request. 

## Lists of library used
- Selenium

## TO-DO

- [x] Find the right library to use (see update on 2022.05.07)
- [ ] Contact school IT to see if they have any resources.
- [ ] Randomize the scraping frequency
- [ ] Scrape data of eviction
- [ ] Convert the data scraped to excel file
- [ ] Update Methodology

## Progress Update

### 2022.05.08
Progress: date box cleared; date string generate script completed
Problem: tag indicates that it's hidden

Error Message (using firefox):

```
Traceback (most recent call last):
  File "Scraper.py", line 44, in <module>
    driver.find_element(by = By.XPATH, value = xpath_date_box).send_keys("01012022" + Keys.ENTER).perform()
  File "/opt/anaconda3/lib/python3.8/site-packages/selenium/webdriver/remote/webelement.py", line 570, in send_keys
    self._execute(Command.SEND_KEYS_TO_ELEMENT,
  File "/opt/anaconda3/lib/python3.8/site-packages/selenium/webdriver/remote/webelement.py", line 740, in _execute
    return self._parent.execute(command, params)
  File "/opt/anaconda3/lib/python3.8/site-packages/selenium/webdriver/remote/webdriver.py", line 430, in execute
    self.error_handler.check_response(response)
  File "/opt/anaconda3/lib/python3.8/site-packages/selenium/webdriver/remote/errorhandler.py", line 247, in check_response
    raise exception_class(message, screen, stacktrace)
selenium.common.exceptions.ElementNotInteractableException: Message: Element <td> is not reachable by keyboard
```
Error Messagae (using chrome):

```
Get LATEST chromedriver version for 101.0.4951 google-chrome
Driver [/Users/.wdm/drivers/chromedriver/mac64/101.0.4951.41/chromedriver] found in cache
Traceback (most recent call last):
  File "Scraper.py", line 42, in <module>
    driver.find_element(by = By.XPATH, value = xpath_date_box).send_keys("01012022" + Keys.ENTER).perform()
  File "/opt/anaconda3/lib/python3.8/site-packages/selenium/webdriver/remote/webelement.py", line 570, in send_keys
    self._execute(Command.SEND_KEYS_TO_ELEMENT,
  File "/opt/anaconda3/lib/python3.8/site-packages/selenium/webdriver/remote/webelement.py", line 740, in _execute
    return self._parent.execute(command, params)
  File "/opt/anaconda3/lib/python3.8/site-packages/selenium/webdriver/remote/webdriver.py", line 430, in execute
    self.error_handler.check_response(response)
  File "/opt/anaconda3/lib/python3.8/site-packages/selenium/webdriver/remote/errorhandler.py", line 247, in check_response
    raise exception_class(message, screen, stacktrace)
selenium.common.exceptions.ElementNotInteractableException: Message: element not interactable
  (Session info: chrome=101.0.4951.54)
Stacktrace:
0   chromedriver                        0x00000001033692c9 chromedriver + 5120713
1   chromedriver                        0x00000001032f7e33 chromedriver + 4656691
2   chromedriver                        0x0000000102ee700f chromedriver + 393231
3   chromedriver                        0x0000000102f161af chromedriver + 586159
4   chromedriver                        0x0000000102f1579d chromedriver + 583581
5   chromedriver                        0x0000000102f39482 chromedriver + 730242
6   chromedriver                        0x0000000102f10b05 chromedriver + 563973
7   chromedriver                        0x0000000102f3958e chromedriver + 730510
8   chromedriver                        0x0000000102f4bf41 chromedriver + 806721
9   chromedriver                        0x0000000102f39373 chromedriver + 729971
10  chromedriver                        0x0000000102f0f609 chromedriver + 558601
11  chromedriver                        0x0000000102f10635 chromedriver + 562741
12  chromedriver                        0x000000010333bb1d chromedriver + 4934429
13  chromedriver                        0x0000000103340295 chromedriver + 4952725
14  chromedriver                        0x00000001033453cf chromedriver + 4973519
15  chromedriver                        0x0000000103340cba chromedriver + 4955322
16  chromedriver                        0x000000010331b37c chromedriver + 4801404
17  chromedriver                        0x000000010335ac68 chromedriver + 5061736
18  chromedriver                        0x000000010335adef chromedriver + 5062127
19  chromedriver                        0x00000001033705e5 chromedriver + 5150181
20  libsystem_pthread.dylib             0x00007ff8130c64e1 _pthread_start + 125
21  libsystem_pthread.dylib             0x00007ff8130c1f6b thread_start + 15
```


### 2022.05.07
Initiated the web browser using selenium  

## Useful Links and Sources Consulted
- Selenium Documentation: https://www.selenium.dev/documentation/
- Web driver Documentation: https://w3c.github.io/webdriver/#is-element-selected 


---

Shield: [![CC BY-SA 4.0][cc-by-sa-shield]][cc-by-sa]

This work is licensed under a
[Creative Commons Attribution-ShareAlike 4.0 International License][cc-by-sa].

[![CC BY-SA 4.0][cc-by-sa-image]][cc-by-sa]

[cc-by-sa]: http://creativecommons.org/licenses/by-sa/4.0/
[cc-by-sa-image]: https://licensebuttons.net/l/by-sa/4.0/88x31.png
[cc-by-sa-shield]: https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg


AKA No commercial use. 
