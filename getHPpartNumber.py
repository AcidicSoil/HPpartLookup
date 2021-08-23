from selenium import webdriver
import re
import bs4
import requests
import webbrowser
import sys
import pyperclip

browser = webdriver.Firefox()
browser.get('https://partsurfer.hp.com/Search.aspx')

acceptCookies = browser.find_element_by_id('onetrust-accept-btn-handler')
pyautogui.click(693, 362)

searchElem = browser.find_element_by_name(
    "ctl00$BodyContentPlaceHolder$SearchText$TextBox1")
print("Enter hp serial number" + input())
searchElem.send_keys('8cg7222dcd')
searchElem.submit()

def getHPpartNumber(productUrl):
    res = requests.get(productUrl)
    res.raise_for_status()
