from selenium import webdriver 
from selenium.webdriver.common.keys import Keys 
import sys, pyperclip
import time 
from selenium.webdriver.support import expected_conditions as EC


#fillout form 1 
url = 'https://www.dhl.de/de/privatkunden/pakete-versenden/online-frankieren.html?type=ShipmentEditor'
browser = webdriver.Firefox()
browser.get(url)


both = {'#address\.sender\.name2': 'Roman Kondratiev',
		'#address\.sender\.street': 'Waldstr.',
		'#address\.sender\.streetNumber': '48',
		'#address\.sender\.plz': '10551',
		'#address\.sender\.city': 'Berlin',
		'#address\.sender\.email': 'romhedoo@gmail.com'}

for i,y in both.items():
	elem = browser.find_element_by_css_selector(i)
	elem.send_keys(y)


#fillout form 2 
elem7 = browser.find_element_by_css_selector('#address\.receiver\.name2')
elem7.send_keys(sys.argv[1] +' '+ sys.argv[2])
elem8 = browser.find_element_by_css_selector('#address\.receiver\.street')
elem8.send_keys(sys.argv[3])
elem9 = browser.find_element_by_css_selector('#address\.receiver\.streetNumber')
elem9.send_keys(sys.argv[4])
elem10 = browser.find_element_by_css_selector('#address\.receiver\.plz')
elem10.send_keys(sys.argv[5])
elem11 = browser.find_element_by_css_selector('#address\.receiver\.city')
elem11.send_keys(sys.argv[6])

#click buttoms 
try: 
	elem12 = browser.find_element_by_css_selector('html.js.flexbox.flexboxlegacy.rgba.opacity.csscolumns.multiplebgs.csstransforms.cssgradients body div.main.integrationpage div#application div.dhl.redesign.frankieren main#content.mm_content div.dhl.redesign.frankieren form#ProductOrderForm section.mm_section.mm_section-secondary div.container div.mm_buttons.mm_buttons-full-width a#onOk.btn.btn-primary.submit')
	elem12.click()
	wait = WebDriverWait(driver, 5)
	#element = wait.until(EC.element_to_be_clickable((By.ID, 'button.btn.btn-primary')))
	elem13 = browser.find_element_by_css_selector('div.mm_buttons:nth-child(1) > button:nth-child(2)')
	elem13.click()
	wait = WebDriverWait(driver, 2)
	elem14 = browser.find_element_by_css_selector('#braintreeOption')
	elem14.click()
	elem15 = browser.find_element_by_css_selector('.mm_section-secondary > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > label:nth-child(1) > span:nth-child(2)')
	elem15.click()
except:
	print('No element')




