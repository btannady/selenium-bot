import unittest
from selenium import webdriver
import page



class PythonOrgSearch(unittest.TestCase):

	# for opening up the browser
	def setUp(self):
		self.driver = webdriver.Firefox(executable_path=r"C:\Program Files (x86)\geckodriver.exe")
		self.driver.get("http://www.python.org")

	# ---------------------------------

	# functions beginning with test_ will run 

	def test_search_python(self):
		mainPage = page.MainPage(self.driver)
		assert mainPage.is_title_matches()
		mainPage.search_text_element = "pycon"
		mainPage.click_go_button()
		search_result_page = page.SearchResultPage(self.driver)
		assert search_result_page.is_results_found()


	# ---------------------------------

	# for closing out the tab
	def tearDown(self):
		self.driver.close()


if __name__ == "__main__":
	unittest.main()