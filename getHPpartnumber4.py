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
#8cg7222dcd
page = requests.get('https://partsurfer.hp.com/Search.aspx')
page.raise_for_status()


# Asks user for serial number
print('enter serial number')
#serial_number = input()
serial_number = "8cg7222dcd"
#print('enter item description')
#item = input().upper()

#keywords = [item]
#print(type(keywords))

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
#options.page_load_strategy = 'eager'
options.add_argument('headless')
driver = webdriver.Chrome(
    options=options, executable_path=r'C:/Users/user/mypythonscripts/chromedriver')

driver.get('https://partsurfer.hp.com/Search.aspx')
#driver.manage().window().maximize()
wait = WebDriverWait(driver, 3)

select = Select(driver.find_element_by_name(
    'ctl00$BodyContentPlaceHolder$ddlCountry'))
select.select_by_visible_text('United States')

element = wait.until(EC.element_to_be_clickable(
    (By.XPATH, "// *[@id='onetrust-accept-btn-handler']"))).click()

#alert = driver.switch_to.alert

textElem = driver.find_element_by_name(
    "ctl00$BodyContentPlaceHolder$SearchText$TextBox1")
textElem.send_keys(serial_number)
textElem.submit()
searchElem = driver.find_element_by_xpath(
    "//*[@id='ctl00_BodyContentPlaceHolder_SearchText_btnSubmit']").click()
###
#soup = bs4.BeautifulSoup(driver.page_source, features="lxml")
#tables = soup.find_all(
#    'table', {"id": ["ctl00_BodyContentPlaceHolder_gridSpareBOM"]})
###
#print(type(tables))

#rows = soup.find_all("td", "title")
###
#table = tables[0]
#tab_data = [[cell.text for cell in row.find_all(["th", "td"])]
#            for row in table.find_all("tr")]
###

# Grabs part page current url and turns it into html


url2 = driver.current_url
#print(url2)

req1 = requests.get(url2)
if req1.status_code in [200]:
    html_doc = req1.text
else:
    print('Could not retrieve: % s, err: % s - status code: % s' %
          (url2, req1.text, req1.status_code))
#dfs = pd.read_html(url2)
#print(type(dfs))
#print(dfs)
#def get_all_tabs(URL = url2):
#    driver = webdriver.Chrome()
#    driver.get(URL)
#    print(url2)
#    soup = bs4.BeautifulSoup(driver.page_source, 'lxml')

driver.implicitly_wait(30)
driver.get(url2)
df = pd.read_html(driver.find_element_by_id("ctl00_BodyContentPlaceHolder_gridSpareBOM").get_attribute('outerHTML'))[0]
display(df[['Spare Part Number', 'Spare Part Description']])
df = df[df['Spare Part Description'].str.contains('CABLE, ODD')]
#df1 = pd.read_html(driver.find_element_by_id("ctl00_BodyContentPlaceHolder_gridSpareBOM").get_attribute('outerHTML'))[0]
display(df['Spare Part Number'][3])
#display(df)

#soup = bs4.BeautifulSoup(driver.page_source, features="lxml")    
#tables = soup.find_all('table', {"id": ["ctl00_BodyContentPlaceHolder_gridSpareBOM"]})
#tabs_dic = {}
    
#for table in tables:
#    tab_name = table['id']
#    tab_data = [[cell.text for cell in row.find_all(["th", "td"])]
#                        for row in table.find_all("tr")]
#    df = pd.DataFrame(tab_data)
#    df.columns = df.iloc[0, :]
#    df.drop(index=0, inplace=True)

#    tabs_dic[tab_name] = df
#print(type(df))
#print(type(display(df.to_string())))
#dfs1 = pd.read_html(url2, attrs={"class": "table_sortable  tbl"})
#print(type(dfs1))
#print(dfs1)
sleep(2)
#https://stackoverflow.com/questions/23580726/python-beautifulsoup-list-index-after-the-table
#https://www.crummy.com/software/BeautifulSoup/bs4/doc/
#https://towardsdatascience.com/scrape-tabular-data-with-python-b1dd1aeadfad
driver.close()
#8cg7222dcd
