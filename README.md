# Eviction Case Data Scraping Project

## Introduction 
This project is part of a research sponsored by Charles Center at College of William and Mary in Virginia, United States. Our plan is to create a open-source database of eviction data in Williamsburg and James City County. This involves web scraping from online docket (http://ewsocis1.courts.state.va.us/CJISWeb/circuit.jsp) and manually gather information from the court. A more detailed and accurate methodology would be updated later.

## TO-DO

- [x] Find the right library to use (see update on 2022.05.07)
- [x] Randomize the scraping frequency
- [ ] Scrape data of eviction
- [x] Convert the data scraped to excel file
- [ ] Update Methodology

## Progress Update


### 2022.06.23   
Scraping case summary completed

### 2020.05.15
hidden tag problem resolvd (copy the full xpath)

### 2022.05.08
Progress: date box cleared; date string generate script completed
Problem: tag indicates that it's hidden

### 2022.05.07
Initiated the web browser using selenium  

## Useful Links and Sources Consulted
- Selenium Documentation: https://www.selenium.dev/documentation/
- Web driver Documentation: https://w3c.github.io/webdriver/#is-element-selected 

## On Eviction

- [The Scarlet E: Unmasking America’s Eviction Crisis](https://www.wnycstudios.org/podcasts/otm/scarlet-e-unmasking-americas-eviction-crisis)
- [Inaccuracies in Eviction Records: Implications for Renters and Researchers](https://www.tandfonline.com/doi/full/10.1080/10511482.2020.1748084)

---

Shield: [![CC BY-SA 4.0][cc-by-sa-shield]][cc-by-sa]

This work is licensed under a
[Creative Commons Attribution-ShareAlike 4.0 International License][cc-by-sa].

[![CC BY-SA 4.0][cc-by-sa-image]][cc-by-sa]

[cc-by-sa]: http://creativecommons.org/licenses/by-sa/4.0/
[cc-by-sa-image]: https://licensebuttons.net/l/by-sa/4.0/88x31.png
[cc-by-sa-shield]: https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg


AKA No commercial use. 
