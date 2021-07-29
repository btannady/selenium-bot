
from selenium import webdriver

PATH = "C:\Program Files (x86)\geckodriver.exe"
driver = webdriver.Firefox(executable_path=r"C:\Program Files (x86)\geckodriver.exe")

driver.get("https://github.com/btannady/projects")

driver.close() # closes the current tab
