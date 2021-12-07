from typing import Pattern
from urllib import parse
from requests.models import Response
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import re
from re import match
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
from urllib.parse import urlparse
import urllib.request
from itertools import chain
username = os.getlogin()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(
    options=options, executable_path=r'C:/Users/' + username + '/mypythonscripts/chromedriver')
list_of_links = []
def main():
    #page = requests.get('https://www.google.com/')
    #page.raise_for_status()

    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    options.add_experimental_option("detach", True)
    #Runs selenium in the background
    #options.add_argument('headless')
    
    #Goes to URL home page
    driver.get('https://www.google.com/search?q=allintext%3A926482-001+site%3Aebay.com&rlz=1C1CHBF_enUS902US902&oq=allintext%3A926482-001+site%3Aebay.com&aqs=chrome..69i57j69i58.793j0j15&sourceid=chrome&ie=UTF-8')
    wait = WebDriverWait(driver, 30)
    #Search_bar = driver.find_element_by_name(
     #   "q")

    #Inputs part number and vendor site in search box
    #Search_bar.send_keys("allintext:926482-001 site:ebay.com", Keys.ENTER)

    get_href_link_list()
    get_ebay_links()

def get_href_link_list():
    soup = BeautifulSoup(driver.page_source, features='lxml')
    for a_tag in soup.find_all('a'):
        href_list = (a_tag.get('href'))
        list_of_links.append(str(href_list))

def get_ebay_links():
    new_list = [s[12:16] for s in list_of_links]
    # creates a list idx_list and enumerates a list of substringed values from list_of_links
    # if ebay is in list it appends the index to idx_list. 
    idx_list = []
    for idx, item in enumerate(new_list):
            if "ebay" in item:
                idx_list.append(f"{idx}")
    #print(idx_list)
    # Finds the start and end of the indexes that have the proper links that will be needed for a range call.
    idx_range_start = int(idx_list[0])
    idx_range_end = int(idx_list[-1])
    #print(idx_range_end, idx_range_start)
    #print(list_of_links[idx_range_start:idx_range_end])
    for link in list_of_links[idx_range_start:idx_range_end]:
        #driver.get(link)
        #getEbayPrice(link)
        price = ("The price is: " + getEbayPrice(link))
        print(price)

def getEbayPrice(productUrl):
    res = requests.get(productUrl)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    selector1 = (bool(soup.select('#prcIsum')))
    selector2 = (bool(soup.select(
        '#s0-0-18-5-12-26-50 > div > span.item-price > div')))
    if selector1 == True:
        elems = soup.select('#prcIsum')
    elif selector2 == True:
        elems = soup.select(
            '#s0-0-18-5-12-26-50 > div > span.item-price > div')
    return elems[0].text.strip()

main()
sleep(2)
driver.close()
