from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from logic.base_app_page import BaseAppPage


class MyAssetsPage(BaseAppPage):
    PACKAGES_NAME = '//div[@data-test="package-name"]'

    def __init__(self, driver):
        """
        Initialize the LoginPage with a WebDriver instance.

        :param driver: The WebDriver instance to use for browser interactions.
        """
        super().__init__(driver)

    def get_assets_name(self):
        """
        Retrieves the names of all assets displayed on the current page.

        This method refreshes the page, waits for the asset name elements to be present,
        and then collects and returns the text of these elements as a list.

        :return: A list of asset names displayed on the current page.
        """
        self.refresh_page()
        elements = WebDriverWait(self._driver, 5).until(
            EC.presence_of_all_elements_located((By.XPATH, self.PACKAGES_NAME)))
        category_names = [element.text for element in elements]
        return category_names
