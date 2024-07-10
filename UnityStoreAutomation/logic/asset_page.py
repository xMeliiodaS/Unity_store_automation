from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from logic.base_app_page import BaseAppPage


class AssetPage(BaseAppPage):
    ADD_TO_CART_BUTTON = '//div[@id="product-detail-add-to-cart-button-v2"]'
    ASSET_TITLE = '//h1'

    def __init__(self, driver):
        super().__init__(driver)

    def click_on_add_to_cart_button(self):
        """
        Click on the add to cart button.
        """
        element = WebDriverWait(self._driver, 5).until(
            EC.presence_of_element_located((By.XPATH, self.ADD_TO_CART_BUTTON)))
        element.click()

    def get_asset_title(self):
        """
        """
        return WebDriverWait(self._driver, 5).until(
            EC.presence_of_element_located((By.XPATH, self.ASSET_TITLE))).text

    def add_asset_to_cart_flow(self):
        """
        Add asset to the cart, then view the cart.
        """
        self.click_on_add_to_cart_button()
        self.click_view_cart_button()
