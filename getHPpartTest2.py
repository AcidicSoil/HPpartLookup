from typing import Pattern
from requests.models import Response
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import re
import bs4
from bs4 import BeautifulSoup
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


def main():
    page = requests.get('https://www.google.com/')
    page.raise_for_status()
    username = os.getlogin()
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    options.add_experimental_option("detach", True)
    #Runs selenium in the background
    #options.add_argument('headless')

    #Finds path to chrome driver
    driver = webdriver.Chrome(
        options=options, executable_path=r'C:/Users/'+ username + '/mypythonscripts/chromedriver')
    
    #Goes to URL home page
    driver.get('https://www.google.com/')
    wait = WebDriverWait(driver, 30)
    Search_bar = driver.find_element_by_name(
        "q")

    #Inputs part number and vendor site in search box
    Search_bar.send_keys("allintext:926482-001 site:ebay.com", Keys.ENTER)
    soup = BeautifulSoup(driver.page_source, features='lxml')
    wait

    test = soup.find_all(href=not_ebay)
    print(test)
    sleep(2)
    driver.close()
##################################################################################
# New function here


def not_ebay(href):
    return href and not re.compile("google.com").search(href)


    #for link in soup.find_all('a'):
    #    print(link.get('href'))
    
    #links = soup.find_all('a')
    
    #driver.get(url2)
    
    #driver.implicitly_wait(30)
    
    #lnks = []
    #lnks=driver.find_elements_by_tag_name("a")
    
    #for lnk in lnks:
    #    print(lnk.get_attribute('href'))
    #links.append(lis.get_attribute('href'))
    #for link in links:
    #    driver.get(link)
    #sleep(3)
    #print(links)
    #elems = driver.find_elements_by_tag_name('a')
    #for elem in elems:
    #    href = elem.get_attribute('href')
    #    if href is not None:
    #        print(href)


main()
