import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from logic.base_app_page import BaseAppPage
from logic.utils import Utils


class HomePage(BaseAppPage):
    ASSET_LINK = '(//div[@data-test="package-title"])[2]'
    SUB_CATEGORIES = '//a[@class="_1oxj5"]'

    def __init__(self, driver):
        super().__init__(driver)

    def click_on_asset_link(self):
        """
        Click on the asset link.
        """
        element = WebDriverWait(self._driver, 8).until(
            EC.element_to_be_clickable((By.XPATH, self.ASSET_LINK)))
        self.scroll_to_element(element)
        element.click()

    def click_on_category_by_name(self, name):
        """
        Clicks on a random category and returns its name.
        """
        element = WebDriverWait(self._driver, 5).until(
            EC.presence_of_element_located((By.XPATH, f'//a[text()="{name}"]')))
        element.click()

    def get_random_category_text(self):
        random_index = Utils.generate_random_number() - 1
        elements = WebDriverWait(self._driver, 5).until(
            EC.presence_of_all_elements_located((By.XPATH, self.SUB_CATEGORIES)))
        return elements[random_index].text
