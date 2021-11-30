from requests.models import Response
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import bs4
from bs4 import BeautifulSoup
import requests
import webbrowser
import sys
import pandas as pd
import html5lib
from selenium.common.exceptions import NoSuchCookieException, NoSuchElementException
from selenium.webdriver.support.ui import Select
from time import sleep
import numpy as np
import os
import urllib.request
from selenium.common.exceptions import *

username = os.getlogin()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(
    options=options, executable_path=r'C:/Users/' + username + '/mypythonscripts/chromedriver')
options.add_experimental_option("excludeSwitches", ["enable-logging"])
options.add_experimental_option("detach", True)
#Runs selenium in the background
options.add_argument('headless')
list_of_links = []
price_list = []

def main():
    getEbayPrice()

def get_ebay_links():
    for cite_tag in driver.find_elements_by_tag_name("cite"):
        cite_tag.click()
        getEbayPrice(driver.current_url)

def getEbayPrice(url): 
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elems = soup.select('#prcIsum')
    return elems

price = getEbayPrice('https://www.ebay.com/p/28022853255')
print('The price is ' + price)
main()
