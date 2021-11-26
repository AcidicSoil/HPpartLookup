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
username = os.getlogin()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(
    options=options, executable_path=r'C:/Users/' + username + '/mypythonscripts/chromedriver')
list_of_links = []
cleaned_list_of_links = []
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
    
   # add_links_list()
    #filter_list()
    href_list()
    str_list()
    index_list()
    
def add_links_list():
    lists = driver.find_elements_by_class_name('LC20lb MBeuO DKV0Md')
    
    links = []
    
    for lis in lists:
        print(lis.get_attribute('href'))
        links.append(lis.get_attribute('href'))
    for link in links:
        print(links)
        driver.get(link)
        sleep(3)

def href_list():
    soup = BeautifulSoup(driver.page_source, features='lxml')
    for a_tag in soup.find_all('a'):
        href_list = [(a_tag.get('href'))]
        list_of_links.append(str(href_list))
        
        #for index, href in enumerate(list_of_links):
        #list_of_links.append(str(href_list))
        #links_to_click = driver.fin
            #print(f"{index}:{href}")
        #print(list_of_links)

def str_list():
    link_index = []
    new_list = [s[14:18] for s in list_of_links]
    for index, item in enumerate(new_list):
        if "ebay" in item:
            newest_list = [(f"{index}")]
            #for index in newest_list:
                
            list_of_links.append(newest_list)
            
            #print(newest_list)


def index_list():
    soup = BeautifulSoup(driver.page_source, features='lxml')
    for a_tag in soup.find_all('a'):
        href_list = [(a_tag.get('href'))]
        
        for index, href in enumerate(list_of_links):
            
            print(f"{index}")
            
            # use code below after I index list of hrefs
            for i in list_of_links:
                if index == i:
                    wait = WebDriverWait(driver, 10)
                    element = wait.until(EC.element_to_be_clickable((By.href, href)))
                #click index valued link
                
                #print(cleaned_list_of_links)
            #print(cleaned_list_of_links)
        #for index, href in enumerate(list_of_links):
        #    indexed_link_list = 

    #for item in new_list:
    #    r = re.compile('y$')
    #    if any(r.match(item) for item in new_list):
    #        print(item)
    #for index, item in enumerate(new_list):
    #    print(f"{index}: {item}")
        
#def filter_list():    
#    for element in list_of_links:
#        o = urlparse(element)
#        o.netloc
#        new_list = []
#        list_of_links.append(new_list)
#        for element in list_of_links:
#            print(element)
#filtered_list = [o.(x) for x in list_of_links]
        #o = urlparse(url)
        #o.netloc(url)
#(?P<https>\w\w\w):..(?P<www>\w+).(?P<site>\w+).(?P<domain>\w+)
       
main()
sleep(2)
driver.close()
