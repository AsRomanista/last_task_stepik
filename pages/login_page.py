from .base_page import BasePage
from .locators import LoginPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage(BasePage):
    def register_new_user(self, email, password):
        WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located(LoginPageLocators.REGISTRATION_EMAIL_INPUT)
        )

        email_input = self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL_INPUT)
        password_input = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD_INPUT)
        password_confirmation_input = self.browser.find_element(*LoginPageLocators.REGISTRATION_CONFIRM_PASSWORD_INPUT)
        register_button = self.browser.find_element(*LoginPageLocators.REGISTRATION_SUBMIT_BUTTON)

        email_input.send_keys(email)
        password_input.send_keys(password)
        password_confirmation_input.send_keys(password)
        register_button.click()
