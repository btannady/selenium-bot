
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 

import time

# sets up webdriver pathing
PATH = "C:\Program Files (x86)\geckodriver.exe"
driver = webdriver.Firefox(executable_path=r"C:\Program Files (x86)\geckodriver.exe")

# ---------------------------------------

# open up desired url
driver.get("https://techwithtim.net")

print(driver.title)

# --------------------------------------

# navigate to desired location on page
curr_title = driver.title
search = driver.find_element_by_name("s")
search.send_keys("test")
search.send_keys(Keys.RETURN)
time.sleep(2)

# attempt to scrape desired information on current page
try: 
	# wait a maximum of 10 seconds until expected element is located
	main = WebDriverWait(driver, 10).until(
		EC.presence_of_element_located((By.ID, "main"))
	)

	print(main.text)

finally:
	driver.quit()

