
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 

import time

# ---------------------------------------

# sets up webdriver pathing
PATH = "C:\Program Files (x86)\geckodriver.exe"
driver = webdriver.Firefox(executable_path=r"C:\Program Files (x86)\geckodriver.exe")

# ---------------------------------------

# open up desired url
driver.get("https://www.crunchyroll.com/")

print(driver.title)

# --------------------------------------

# navigate to desired location on page
search = driver.find_element_by_id("header_search_input")
search.send_keys("sword")
search.send_keys(Keys.RETURN)

time.sleep(2) # sometimes necessary to give page buffer time to transition

# --------------------------------------

# attempt to scrape desired information on current page WHEN it is available
try: 
	# wait a maximum of 10 seconds until expected element is located
	element = WebDriverWait(driver, 10).until(
		EC.presence_of_element_located((By.LINK_TEXT, "7"))
	)
	element.click()
	time.sleep(1)

	element = WebDriverWait(driver, 10).until(
		EC.presence_of_element_located((By.TAG_NAME, "href"))
	)
	print(element.text)
	


finally:
	driver.quit()
