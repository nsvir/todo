from selenium import webdriver
import unittest, time, re

class NavigationTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://google.fr/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_navigation(self):
        self.search_field = self.driver.find_element_by_name("q")
        self.search_field.send_keys("Selenium WebDriver Interview questions")
        self.search_field.submit()
        lists = self.driver.find_elements_by_class_name("r")
        no=len(lists)
        self.assertEqual(10, len(lists))

if __name__ == '__main__':
    unittest.main()
