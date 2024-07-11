from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from logic.base_app_page import BaseAppPage


class MyAssetsPage(BaseAppPage):
    PACKAGES_NAME = '//div[@data-test="package-name"]'

    def __init__(self, driver):
        super().__init__(driver)

    def get_assets_name(self):
        """
        Clicks on a random category and returns its name.
        """
        self.refresh_page()
        elements = WebDriverWait(self._driver, 5).until(
            EC.presence_of_all_elements_located((By.XPATH, self.PACKAGES_NAME)))
        category_names = [element.text for element in elements]
        return category_names

