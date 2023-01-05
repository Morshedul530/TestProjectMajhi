import unittest

from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from pages.signin_page import SignIn


class CreateAccountTest(unittest.TestCase):
    def test_create_account(self):
        baseURL = "https://www.majhi.app/en"
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(baseURL)
        time.sleep(2)

        signin = SignIn(driver)
        signin.signin_page("01571231339")
        time.sleep(15)

        driver.quit()