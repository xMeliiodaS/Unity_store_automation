import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from logic.base_app_page import BaseAppPage


class PersonalSettingsPage(BaseAppPage):
    EDIT_BIO = '//a[text() = "Edit Bio"]'
    EDIT_BIO_TEXTAREA_INPUT = '//textarea'
    SAVE_BIO_BUTTON = '//button[@label="Save"]'
    CURRENT_BIO_TEXT = '//div[@class="bQU15 e-vlo"]'

    def __init__(self, driver):
        super().__init__(driver)

    def click_on_edit_bio_button(self):
        """
        Clicks on the personal settings button to go to the account settings.
        """
        WebDriverWait(self._driver, 5).until(
            EC.presence_of_element_located((By.XPATH, self.EDIT_BIO))).click()

    def fill_bio_input(self, bio_text):
        """
        Clicks on the personal settings button to go to the account settings.
        """
        element = WebDriverWait(self._driver, 5).until(
            EC.presence_of_element_located((By.XPATH,
                                            self.EDIT_BIO_TEXTAREA_INPUT)))
        time.sleep(1)
        element.clear()
        element.send_keys(bio_text)

    def click_on_save_bio_button(self):
        """
        Clicks on the personal settings button to go to the account settings.
        """
        WebDriverWait(self._driver, 5).until(
            EC.presence_of_element_located((By.XPATH, self.SAVE_BIO_BUTTON))).click()

    def get_current_bio_text(self):
        return WebDriverWait(self._driver, 5).until(
            EC.presence_of_element_located((By.XPATH, self.CURRENT_BIO_TEXT))).text
