from typing import Pattern
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
import bs4
import requests
import webbrowser
import sys
import pyperclip
import pandas as pd
import html5lib
from selenium.common.exceptions import NoSuchCookieException, NoSuchElementException
from selenium.webdriver.support.ui import Select
from time import sleep
from IPython.display import display
import numpy as np
from dataclasses import make_dataclass
import os
#8cg7222dcd
def main():
    page = requests.get('https://partsurfer.hp.com/Search.aspx')
    page.raise_for_status()
    username = os.getlogin()
    
    # Asks user for serial number
    serial_number = input('enter serial number: ')
    #serial_number = "8cg7222dcd"

    #Asks user to enter item 
    item = input('enter item description: ').upper()

    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])

    #Runs selenium in the background
    options.add_argument('headless')

    #Finds path to chrome driver
    driver = webdriver.Chrome(
        options=options, executable_path=r'C:/Users/'+ username + '/mypythonscripts/chromedriver')

    #Goes to URL home page
    driver.get('https://partsurfer.hp.com/Search.aspx')
    wait = WebDriverWait(driver, 3)

    #Selects country
    select = Select(driver.find_element_by_name(
        'ctl00$BodyContentPlaceHolder$ddlCountry'))
    select.select_by_visible_text('United States')

    #Clicks on pop-up dialog box
    element = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "// *[@id='onetrust-accept-btn-handler']"))).click()

    #Finds search box
    textElem = driver.find_element_by_name(
        "ctl00$BodyContentPlaceHolder$SearchText$TextBox1")

    #Inputs serial number in search box
    textElem.send_keys(serial_number)
    #Clicks submit on search box
    textElem.submit()
    searchElem = driver.find_element_by_xpath(
        "//*[@id='ctl00_BodyContentPlaceHolder_SearchText_btnSubmit']").click()
    # Grabs part page current url and turns it into html
    url2 = driver.current_url

    req1 = requests.get(url2)
    if req1.status_code in [200]:
        html_doc = req1.text
    else:
        print('Could not retrieve: % s, err: % s - status code: % s' %
            (url2, req1.text, req1.status_code))

    driver.implicitly_wait(30)
    driver.get(url2)
    df = pd.read_html(driver.find_element_by_id(
        "ctl00_BodyContentPlaceHolder_gridSpareBOM").get_attribute('outerHTML'))[0]
    display(df[['Spare Part Number', 'Spare Part Description']])
    df = df[df['Spare Part Description'].str.contains(item)]
    display(df)
    sleep(2)
    #https://stackoverflow.com/questions/23580726/python-beautifulsoup-list-index-after-the-table
    #https://www.crummy.com/software/BeautifulSoup/bs4/doc/
    #https://towardsdatascience.com/scrape-tabular-data-with-python-b1dd1aeadfad
    driver.close()
    #8cg7222dcd
if __name__ == "__main__":
    main()
