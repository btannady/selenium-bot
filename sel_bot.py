
from selenium import webdriver

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://www.google.com/")

driver.close() # closes the current tab

# driver.quit() # quits the entire browser

# print(driver.title) # returns and prints the current tab title 