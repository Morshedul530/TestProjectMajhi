import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from pages.signin_page import SignIn
from pages.store_page import StoreSelectionPage


class Store_SelectionTest(unittest.TestCase):
    def test_store_selection(self):
        baseURL = "https://www.majhi.app/en"
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(baseURL)
        time.sleep(3)

        signin = SignIn(driver)
        signin.signin_page("01571231339")
        time.sleep(15)

        ssp = StoreSelectionPage(driver)
        ssp.store_selection()
        time.sleep(5)