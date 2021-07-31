import unittest
from selenium import webdriver
import page



class PythonOrgSearch(unittest.TestCase):

	# for opening up the browser
	def setUp(self):
		self.driver = webdriver.Firefox(executable_path=r"C:\Program Files (x86)\geckodriver.exe")
		self.driver.get("http://www.python.org")

	# ---------------------------------

	# tests

	
	def test_title(self):
		mainPage = page.MainPage()
		assert mainPage.is_title_matches()


	# ---------------------------------

	# for closing out the tab
	def tearDown(self):
		self.driver.close()


if __name__ == "__main__":
	unittest.main()