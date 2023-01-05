import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from pages.signin_page import SignIn
from pages.store_page import StoreSelectionPage
from pages.payment_process_page import PaymentProcessPage


class Payment_ProcessTest(unittest.TestCase):
    def test_payment_process(self):
        baseURL = "https://www.majhi.app/en"
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(baseURL)
        time.sleep(3)

        signin = SignIn(driver)
        signin.signin_page("01571231339")
        time.sleep(10)

        ssp = StoreSelectionPage(driver)
        ssp.store_selection()
        time.sleep(5)

        ppp = PaymentProcessPage(driver)
        ppp.payment_process()
        time.sleep(3)