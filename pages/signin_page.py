import time
from selenium.webdriver.common.by import By


class SignIn:
    def __init__(self, driver):
        self.driver = driver

        # Signup as a New Customer
        new_customer = self.driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div/nav/div/div/a[1]/div/p')
        new_customer.click()
        time.sleep(2)

    def signin_page(self, phone):
        # Enter Phone Number
        mobile_number = self.driver.find_element(By.ID, 'phone')
        mobile_number.send_keys(phone)

        # Sign In
        sign = self.driver.find_element(By.XPATH, '//*[@id="right"]/div/div[1]/form/button')
        sign.click()
        time.sleep(10)

        #first_name = self.driver.find_element(By.XPATH, "//input[@id='first_name']")
        # first_name.send_keys("Morshedul")
        # time.sleep(1)
        #
        # last_name = self.driver.find_element(By.XPATH, "//input[@id='last_name']")
        # last_name.send_keys("Shuvo")
        # time.sleep(1)
        #
        # email_address = self.driver.find_element(By.XPATH, "//input[@id='email']")
        # email_address.send_keys("mshuvo530@gmail.com")
        # time.sleep(1)
        #
        # done = self.driver.find_element(By.XPATH, "//button[contains(text(),'Done')]")
        # done.click()
        # time.sleep(2)


