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
    #page = requests.get('https://www.google.com/')
    #page.raise_for_status()


    
    #Goes to URL home page
    driver.get('https://www.google.com/search?q=allintext%3A926482-001+site%3Aebay.com&rlz=1C1CHBF_enUS902US902&oq=allintext%3A926482-001+site%3Aebay.com&aqs=chrome..69i57j69i58.793j0j15&sourceid=chrome&ie=UTF-8')
    wait = WebDriverWait(driver, 30)
    #Search_bar = driver.find_element_by_name(
     #   "q")

    #Inputs part number and vendor site in search box
    #Search_bar.send_keys("allintext:926482-001 site:ebay.com", Keys.ENTER)
    
   # add_links_list()
    #filter_list()
    get_href_link_list()
    get_ebay_links()
    #index_list()
    #click_links_in_list()
    


def get_href_link_list():
    soup = BeautifulSoup(driver.page_source, features='lxml')
    for a_tag in soup.find_all('a'):
        href_list = [(a_tag.get('href'))]
        list_of_links.append(str(href_list))
        
def get_ebay_links():
    new_list = [s[14:18] for s in list_of_links]
    # creates a list idx_list and enumerates a list of substringed values from list_of_links
    # if ebay is in list it appends the index to idx_list. 
    idx_list = []
    for idx, item in enumerate(new_list):
            if "ebay" in item:
                idx_list.append(f"{idx}")
    # Finds the start and end of the indexes that have the proper links that will be needed for a range call.
    idx_range_start = int(idx_list[0])
    idx_range_end = int(idx_list[-1])
    list_of_href_links_to_click = list_of_links[idx_range_start:idx_range_end]
    
    for cite_tag in driver.find_elements_by_tag_name("cite"):
        cite_tag.click()
        getEbayPrice(driver.current_url)
    #cite_tags = driver.find_element_by_tag_name("cite")
    #print(cite_tags)
    #for link in cite_tags:
     #   print(link)       
      #  wait = WebDriverWait(driver, 10)
       # WebDriverWait(driver, 20).until(EC.visibility_of_element_located(
        #    (cite_tags, link))).click()

def getEbayPrice(url): 
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elems = soup.select('#prcIsum')
    return elems[0].text.strip() 
    #print(price_list)
    #driver.back()
    #sleep(2)
   # return elems[0].text.strip()


#price = getEbayPrice(
#    part_Url)
#print('The price is ' + price)
        #searchElem = driver.find_element_by_partial_link_text(link).click()
        #searchElem.get(link)
        
        #print(len(list_of_href_links_to_click))
        #print(type(link))
        #wait = WebDriverWait(driver, 10)
        #driver.get(link)
        #driver.find_elements_by_xpath('//a[starts-with(@href, "https://www.ebay.com")]'.click()
        #try:
        #    element = WebDriverWait(driver, 30).until(
        
        #        EC.presence_of_element_located(
        #            (By.XPATH, '//a[@href="'+link+'"]'))
    #)


      #  finally:
       #     driver.quit()
        #element = wait.until(EC.element_to_be_clickable(
        #    (By.XPATH, '//a[@href="'+link+'"]')))
        #sleep(3)
        #driver.find_elements_by_xpath('//a[@href="'+link+'"]').click()
    #print(list_of_href_links_to_click)
    # I can click links by manually coding the list to a file or a driver function
    # or I can select each link by xpath or css selectors
#def click_links_in_list():
#    get_ebay_links()
#    print(list_of_)
    #for link in list_of_href_links_to_click:
        #print(link)
        #//input[starts-with(@href, 'https://www.ebay.com')]
    #    wait = WebDriverWait(driver, 10)
    #    driver.get(link)
        #driver.find_elements_by_xpath('//a[@href="'+link+'"]').click()
        #element = wait.until(EC.element_to_be_clickable((By.XPATH, '//a[@href="'+link+'"]')))
        ###############
        ##rso > div:nth-child(5) > div > div > div.yuRUbf > a
        ##rso > div:nth-child(4) > div > div > div.yuRUbf > a
        ##rso > div:nth-child(4) > div > div > div.yuRUbf > a
        ##rso > div:nth-child(4) > div > div > div.yuRUbf > a
        #<a href="https://www.ebay.com/itm/NEW-HP-17-AK-17AK17-BS-17BS-Silver-LCD-Back-Cover-926482-001-933291-001-Hinges-/303361512142?_ul=IL" data-ved="2ahUKEwjXkYmS-LT0AhWjlmoFHVSmDpgQFnoECAgQAQ" ping="/url?sa=t&amp;source=web&amp;rct=j&amp;url=https://www.ebay.com/itm/NEW-HP-17-AK-17AK17-BS-17BS-Silver-LCD-Back-Cover-926482-001-933291-001-Hinges-/303361512142%3F_ul%3DIL&amp;ved=2ahUKEwjXkYmS-LT0AhWjlmoFHVSmDpgQFnoECAgQAQ"><br><h3 class="LC20lb MBeuO DKV0Md">NEW HP 17-AK 17AK17-BS 17BS Silver LCD Back Cover ...</h3><div class="TbwUpd NJjxre"><cite class="iUh30 qLRx3b tjvcx" role="text">https://www.ebay.com<span class="dyjrff qzEoUe" role="text"> › itm › NEW-HP-17-AK-17AK17-...</span></cite></div></a>
        #<a href="https://www.ebay.com/itm/NEW-HP-17-AK-17AK17-BS-17BS-Silver-LCD-Back-Cover-926482-001-933291-001-Hinges-/303361512142?_ul=IL" data-ved="2ahUKEwjXkYmS-LT0AhWjlmoFHVSmDpgQFnoECAgQAQ" ping="/url?sa=t&amp;source=web&amp;rct=j&amp;url=https://www.ebay.com/itm/NEW-HP-17-AK-17AK17-BS-17BS-Silver-LCD-Back-Cover-926482-001-933291-001-Hinges-/303361512142%3F_ul%3DIL&amp;ved=2ahUKEwjXkYmS-LT0AhWjlmoFHVSmDpgQFnoECAgQAQ"><br><h3 class="LC20lb MBeuO DKV0Md">NEW HP 17-AK 17AK17-BS 17BS Silver LCD Back Cover ...</h3><div class="TbwUpd NJjxre"><cite class="iUh30 qLRx3b tjvcx" role="text">https://www.ebay.com<span class="dyjrff qzEoUe" role="text"> › itm › NEW-HP-17-AK-17AK17-...</span></cite></div></a>
        #/html/body/div[7]/div/div[10]/div[1]/div/div[2]/div[2]/div/div/div[4]/div/div/div[1]/a
    #//*[@id="rso"]/div[4]/div/div/div[1]/a
    ##########
    #clean_list = []
    #start, end = idx_range_start, idx_range_end
    #if start < end:
    #    list_of_links.extend(range(start, end))
    #    list_of_links.append(end)
    
    #print(idx_range_list[0])
       #     print(indexes)
            #res = [indexes[0], indexes[-1]]
            #print(res)
            #cleaned_list_of_indexes.append(list_of_indexes)
    #print(cleaned_list_of_indexes)
            #for index in newest_list:
            #list_of_links.append()          
            #print(newest_list)
#def index_list():      
    #print(list(range(idx_list[0], idx_list[-1])))
        
        
            #indexed_list = []
            #print(indexed_list)
            
            #print(f"{index}, {href}")
            
            # use code below after I index list of hrefs
            # or index, href in enumerate(list_of_links):
            #    if index == i:
            #        print(i)
                    #wait = WebDriverWait(driver, 10)
                    #element = wait.until(EC.element_to_be_clickable((By.href, href)))
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
