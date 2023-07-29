# product_page.py
from .base_page import BasePage
from selenium.webdriver.common.by import By
import math

class ProductPage(BasePage):
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")
    BASKET_TOTAL_MESSAGE = (By.CSS_SELECTOR, ".alert-info .alertinner strong")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")

    def add_product_to_basket(self):
        add_to_basket_button = self.browser.find_element(*self.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()

    def should_be_success_message(self):
        assert self.is_element_present(*self.SUCCESS_MESSAGE), "Success message is not present"

    def should_be_basket_total_message(self):
        assert self.is_element_present(*self.BASKET_TOTAL_MESSAGE), "Basket total message is not present"

    def should_be_correct_product_name(self):
        product_name = self.browser.find_element(*self.PRODUCT_NAME).text
        success_message = self.browser.find_element(*self.SUCCESS_MESSAGE).text
        assert product_name in success_message, "Product name is not in the success message"

    def should_be_correct_basket_total(self):
        product_price = self.browser.find_element(*self.PRODUCT_PRICE).text
        basket_total_message = self.browser.find_element(*self.BASKET_TOTAL_MESSAGE).text
        assert product_price == basket_total_message, "Basket total is not equal to product price"

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))  # Вычисляем ответ
        alert.send_keys(answer)
        alert.accept()

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*self.SUCCESS_MESSAGE), "Success message is presented, but should not be"

    def should_message_disappear_after_adding_product_to_basket(self):
        assert self.is_disappeared(*self.SUCCESS_MESSAGE), "Success message is still presented, but should disappear"

