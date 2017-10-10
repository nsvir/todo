from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class NavigationTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://google.fr/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_navigation(self):
        driver = self.driver
        driver.get(self.base_url + "quote/00007")
        driver.find_element("lst-ib").click()
        try: self.assertEqual("http://localhost:8080/quotes", driver.current_url)
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_link_text("Accueil").click()
        try: self.assertEqual("http://localhost:8080/", driver.current_url)
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.get(self.base_url + "order/00001")
        driver.find_element_by_link_text("Liste commandes").click()
        try: self.assertEqual("http://localhost:8080/orders", driver.current_url)
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_link_text("Accueil").click()
        try: self.assertEqual("http://localhost:8080/", driver.current_url)
        except AssertionError as e: self.verificationErrors.append(str(e))
