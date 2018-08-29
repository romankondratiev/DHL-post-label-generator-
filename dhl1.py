from selenium import webdriver 
from selenium.webdriver.common.keys import Keys 
import sys, pyperclip
import time 
from selenium.webdriver.support import expected_conditions as EC

url = 'https://www.dhl.de/de/privatkunden.html'
browser = webdriver.Firefox()
browser.get(url)

elem12 = browser.find_element_by_css_selector('li.hiddenMobile:nth-child(6) > a:nth-child(1) > div:nth-child(1) > span:nth-child(1) > svg:nth-child(1)')
elem12.click()

elem13 = browser.find_element_by_css_selector('#recaptcha-anchor')
elem13.click()

