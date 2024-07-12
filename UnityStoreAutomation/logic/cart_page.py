from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from logic.base_app_page import BaseAppPage


class CartPage(BaseAppPage):
    ASSET_IN_CART = '//div[@class="pr_b2"]'

    def __init__(self, driver):
        """
        Initialize the HomePage with a WebDriver instance.

        :param driver: The WebDriver instance to use for browser interactions.
        """
        super().__init__(driver)

    def get_asset_in_cart_title(self):
        """
        Retrieves the title of an asset in the cart.

        This method waits for the asset element to be present in the cart
        and then returns its title text.
        """
        return WebDriverWait(self._driver, 5).until(
            EC.presence_of_element_located((By.XPATH, self.ASSET_IN_CART))).text
