from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from logic.base_app_page import BaseAppPage


class HomePage(BaseAppPage):
    ASSET_LINK = '(//div[@data-test="package-title"])[2]'

    def __init__(self, driver):
        super().__init__(driver)
        self._asset_link = WebDriverWait(self._driver, 5).until(
            EC.presence_of_element_located((By.XPATH, self.ASSET_LINK)))

    def click_on_asset_link(self):
        """
        Click on the asset link.
        """
        self._asset_link.click()
