from selenium import webdriver 
from selenium.webdriver.common.keys import Keys 
import sys, pyperclip
#import time 
from selenium.webdriver.support import expected_conditions as EC


url = 'https://www.dhl.de/popweb/gw2/nepal/ProductOrder.action?insert=false&checkOnInit=false&itemId=0'

browser = webdriver.Firefox()
browser.get(url)

#fill out form 1 
try:
    elem = browser.find_element_by_css_selector('#formModel\.sender\.zip')
    elem.send_keys('10551')
    elem2 = browser.find_element_by_css_selector('#formModel\.sender\.name')
    elem2.send_keys('Roman Kondratiev')
    elem3 = browser.find_element_by_css_selector('#formModel\.sender\.houseNumber')
    elem3.send_keys('48')
    elem4 = browser.find_element_by_css_selector('#formModel\.sender\.street')
    elem4.send_keys('Waldstr.')
    elem5 = browser.find_element_by_css_selector('#formModel\.sender\.city')
    elem5.send_keys('Berlin')
    elem6 = browser.find_element_by_css_selector('#formModel\.email')
    elem6.send_keys('romhedoo@gmail.com')
    print('Found <%s> element with that class name!' % (elem.tag_name))
except:
    print('Was not able to find an element with that name.')

#fillout form 2 


elem7 = browser.find_element_by_css_selector('#formModel\.receiver\.name')
elem7.send_keys(sys.argv[1] +' '+ sys.argv[2])
elem8 = browser.find_element_by_css_selector('#formModel\.receiver\.street')
elem8.send_keys(sys.argv[3])
elem9 = browser.find_element_by_css_selector('#formModel\.receiver\.houseNumber')
elem9.send_keys(sys.argv[4])
elem10 = browser.find_element_by_css_selector('#formModel\.receiver\.zip')
elem10.send_keys(sys.argv[5])
elem11 = browser.find_element_by_css_selector('#formModel\.receiver\.city')
elem11.send_keys(sys.argv[6])
#click button 1
try: 
	elem12 = browser.find_element_by_css_selector('html.js.flexbox.flexboxlegacy.rgba.opacity.csscolumns.multiplebgs.csstransforms.cssgradients body div.main.integrationpage div#application div.dhl.redesign.frankieren main#content.mm_content div.dhl.redesign.frankieren form#ProductOrderForm section.mm_section.mm_section-secondary div.container div.mm_buttons.mm_buttons-full-width a#onOk.btn.btn-primary.submit')
	elem12.click()
	#wait = WebDriverWait(driver, 5)
	#element = wait.until(EC.element_to_be_clickable((By.ID, 'button.btn.btn-primary')))
	elem13 = browser.find_element_by_css_selector('div.mm_buttons:nth-child(1) > button:nth-child(2)')
	elem13.click()
	#wait = WebDriverWait(driver, 2)
	elem14 = browser.find_element_by_css_selector('#braintreeOption')
	elem14.click()
	elem15 = browser.find_element_by_css_selector('.mm_section-secondary > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > label:nth-child(1) > span:nth-child(2)')
	elem15.click()
except:
	print('No element')
