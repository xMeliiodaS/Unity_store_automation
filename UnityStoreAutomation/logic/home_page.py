from selenium.webdriver.common.by import By
from infra.base_page import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage(BasePage):
    ACCOUNT_BUTTON = '//button[@class="button right-nav-element"]'
    SIGN_IN_BUTTON = '//div[@class="_2zqSQ"]'

    def __init__(self, driver):
        super().__init__(driver)

    def click_on_account_button(self):
        element = WebDriverWait(self._driver, 5).until(
            EC.presence_of_element_located((By.XPATH, self.ACCOUNT_BUTTON)))
        element.click()

    def click_on_sign_in_button(self):
        element = WebDriverWait(self._driver, 5).until(
            EC.presence_of_element_located((By.XPATH, self.SIGN_IN_BUTTON)))
        element.click()


