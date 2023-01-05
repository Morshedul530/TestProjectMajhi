import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class PaymentProcessPage:
    def __init__(self, driver):
        self.driver = driver

    def payment_process(self):
        shipping_address = self.driver.find_element(By.XPATH, "//p[@type='button']")
        shipping_address.click()
        time.sleep(2)

        first_name = self.driver.find_element(By.XPATH, "//div[@class='w-100 d-flex justify-content-between first-row']//div[1]//input[1]")
        first_name.clear()
        first_name.send_keys('Islam')

        last_name = self.driver.find_element(By.XPATH, '//*[@id="AddShippingAddressModal"]/div/div/div[2]/div[1]/div[2]/input')
        last_name.clear()
        last_name.send_keys('m')

        contact_num = self.driver.find_element(By.XPATH, "//div[@class='wd-30']//input[@type='number']")
        contact_num.clear()
        contact_num.send_keys('')

        division = self.driver.find_element(By.ID, 'cars')
        sel = Select(division)
        sel.select_by_value('0')

        city = self.driver.find_element(By.ID, 'cars')
        sel = Select(city)
        sel.select_by_value('0')

        area = self.driver.find_element(By.ID, 'cars')
        sel = Select(area)
        sel.select_by_value('0')

        address = self.driver.find_element(By.XPATH, "//input[@class='border-radius-8 w-100 p-2']")
        address.clear()
        address.send_keys('')

        postcode = self.driver.find_element(By.XPATH, "//div[@class='forth-row d-flex justify-content-start w-100 pt-3']//div//input[@type='number']")
        postcode.clear()
        postcode.send_keys('8')

        save_btn = self.driver.find_element(By.XPATH, "//button[@class='btn bg_global_secondary_color1 text-white padding_horizontal_3rem pdiing_top_1rem pdiing_bottom_1rem ms-3']")
        save_btn.click()
        time.sleep(2)

        #  Proceed to pay
        proceed_to_pay = self.driver.find_element(By.XPATH, '//*[@id="main"]/div/div[2]/div[2]/div/div[1]/div[3]/button')
        proceed_to_pay.click()
        time.sleep(2)

        #  Click on pay again
        proceed_to_pay = self.driver.find_element(By.XPATH, '//*[@id="main"]/div/div[2]/div[2]/div/div[1]/div[3]/button')
        proceed_to_pay.click()
        time.sleep(2)

        verified_message = self.driver.find_element(By.XPATH, '//*[@id="swal2-title"]/span')
        time.sleep(4)

        display = verified_message.is_displayed()
        if display is True:
            print('Congratulations! Your order has been confirmed')
        else:
            print('Payment is not successful')
