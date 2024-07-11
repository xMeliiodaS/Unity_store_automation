import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from logic.base_app_page import BaseAppPage
from logic.home_page import HomePage
from logic.utils import Utils


class AssetPage(BaseAppPage):
    ADD_TO_CART_BUTTON = '//div[@id="product-detail-add-to-cart-button-v2"]'
    ASSET_TITLE = '//h1'
    CATEGORIES_LIST = '//a[@class="zJTLn breadcrumb-nav-element"]'

    ADD_TO_MY_ASSETS_BUTTON = '//div[@id="product-detail-add-to-cart-button-v2"]'
    ACCEPT_BUTTON = '//button[@label="Accept"]'
    GO_TO_MY_ASSETS = '//div[text() = "Go to My Assets"]'

    def __init__(self, driver):
        super().__init__(driver)
        self._asset_title = self._driver.find_element(By.XPATH, self.ASSET_TITLE)

    def click_on_add_to_cart_button(self):
        """
        Click on the add to cart button.
        """
        element = WebDriverWait(self._driver, 5).until(
            EC.presence_of_element_located((By.XPATH, self.ADD_TO_CART_BUTTON)))
        self.scroll_to_element(element)
        element.click()

    def get_asset_title(self):
        """
        Get the title of the asset.
        """
        return WebDriverWait(self._driver, 5).until(
            EC.presence_of_element_located((By.XPATH, self.ASSET_TITLE))).text

    def add_asset_to_cart_flow(self):
        """
        Adds the asset to the cart and then view the cart.
        """
        self.click_on_add_to_cart_button()
        self.click_view_cart_button()

    def get_asset_path_categories_list_names(self):
        """
        Returns a list of asset path categories names.
        """
        elements = WebDriverWait(self._driver, 5).until(
            EC.presence_of_all_elements_located((By.XPATH, self.CATEGORIES_LIST))
        )
        category_names = [element.text for element in elements]
        return category_names

    def click_on_add_to_my_assets_button(self):
        """
        Clicks on a random category and returns its name.
        """
        element = WebDriverWait(self._driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, self.ADD_TO_MY_ASSETS_BUTTON)))
        time.sleep(2)
        element.click()

    def click_on_accept_to_my_assets_button(self):
        """
        Clicks on a random category and returns its name.
        """
        element = WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.ACCEPT_BUTTON)))
        time.sleep(2)
        element.click()

    # def click_on_go_to_my_assets_button(self):
    #     """
    #     Clicks on a random category and returns its name.
    #     """
    #     element = WebDriverWait(self._driver, 10).until(
    #         EC.element_to_be_clickable((By.XPATH, self.GO_TO_MY_ASSETS)))
    #     time.sleep(2)
    #     element.click()

