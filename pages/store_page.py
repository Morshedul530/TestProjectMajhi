import time
from selenium.webdriver.common.by import By


class StoreSelectionPage:
    def __init__(self, driver):
        self.driver = driver

    def store_selection(self):
        # Store Selection Page
        stores = self.driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div/div[2]/div/div[2]/div/div[1]/a/div/div[1]/img')
        stores.click()
        time.sleep(3)

        # Add the first product
        fpa = self.driver.find_element(By.XPATH, "//div[@class='right-content']//div//div[1]//div[2]//div[2]//div[1]//div[1]//div[3]//div[1]//img[1]")
        fpa.click()
        time.sleep(2)

        verified_message = self.driver.find_element(By.XPATH, '/html/body/div[2]/div')
        time.sleep(4)

        # display = verified_message.is_displayed()
        # if display is True:
        #     print('Product successfully added to cart')
        # else:
        #     print('Product not added')

        # Add the second product
        spa = self.driver.find_element(By.XPATH, "//div[@class='right-content']//div//div[1]//div[2]//div[2]//div[1]//div[1]//div[3]//div[1]//img[1]")
        spa.click()
        time.sleep(2)

        # View Cart
        view_cart = self.driver.find_element(By.XPATH, '//*[@id="header"]/div/div/div[2]/div/div/div[2]/div[2]/div[1]/img')
        view_cart.click()
        time.sleep(3)

        # Click Product
        product = self.driver.find_element(By.XPATH, "//p[@class='mb-1']")
        product.click()
        time.sleep(2)

        ip = self.driver.find_element(By.XPATH, "//div[@class='border border-right-radius-8 product-details-quanity-img-holder d-flex justify-content-center align-items-center make-cursor']//img")
        ip.click()
        time.sleep(3)

        add_cart = self.driver.find_element(By.XPATH, '//*[@id="main"]/div/div/div[2]/div/div/div[6]/div[2]/div[1]/button')
        add_cart.click()
        time.sleep(2)

        popup_message = self.driver.find_element(By.XPATH, "//button[normalize-space()='Ok']")
        time.sleep(2)

        display = popup_message.is_displayed()
        if display is True:
            print('Quantity not available in stock')
        else:
            print('Stock Available')

        ok_btn = self.driver.find_element(By.XPATH, "//button[normalize-space()='Ok']")
        ok_btn.click()
        time.sleep(2)

        # View Cart
        view_cart = self.driver.find_element(By.XPATH, '//*[@id="header"]/div/div/div[2]/div/div/div[2]/div[2]/div[1]/img')
        view_cart.click()
        time.sleep(2)

        #  Go to checkout
        proceed_to_checkout = self.driver.find_element(By.XPATH, "//a[normalize-space()='Proceed to Checkout']")
        proceed_to_checkout.click()
        time.sleep(2)
