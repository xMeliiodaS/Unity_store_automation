import logging
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from logic.base_app_page import BaseAppPage
from infra.logging_setup import logger_setup


class AssetPage(BaseAppPage):
    # ------------------Locators related to the asset's buttons------------------
    ADD_TO_CART_BUTTON = '//div[@id="product-detail-add-to-cart-button-v2"]'
    ASSET_TITLE = '//h1'
    CATEGORIES_PATH_LIST = '//a[@class="zJTLn breadcrumb-nav-element"]'

    # ------------------Related to the process of purchasing the asset------------------
    ADD_TO_MY_ASSETS_BUTTON = '//div[@id="product-detail-add-to-cart-button-v2"]'
    ACCEPT_BUTTON = '//button[@label="Accept"]'

    def __init__(self, driver):
        """
        Initialize the Base App Page with a WebDriver instance.

        :param driver: The WebDriver instance to use for browser interactions.
        """
        super().__init__(driver)

    def click_on_add_to_cart_button(self):
        """
        Click on the add to cart button.
        """
        time.sleep(1.5)
        element = WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.ADD_TO_CART_BUTTON)))
        self.scroll_to_element(element)
        element.click()
        logging.info("Click on Add to cart icon")

    def get_asset_title(self):
        """
        Retrieve the title of the asset.
        """
        return WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.ASSET_TITLE))).text

    def add_asset_to_cart_flow(self):
        """
        Adds the asset to the cart and then navigates to view the cart.
        """
        self.click_on_add_to_cart_button()
        self.click_view_cart_button()

    def get_asset_path_categories_list_names(self):
        """
        Returns a list of names of the asset path categories.
        """
        elements = WebDriverWait(self._driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, self.CATEGORIES_PATH_LIST))
        )

        # Get text from each element in the list
        category_names = list(map(lambda element: element.text, elements))
        return category_names

    def click_on_add_to_my_assets_button(self):
        """
        Clicks on the 'Add to My Assets' button after waiting for it to be clickable.
        """
        element = WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.ADD_TO_MY_ASSETS_BUTTON)))
        time.sleep(2)
        element.click()
        logging.info("Clicked on the 'Add to My Assets' button")

    def click_on_accept_to_my_assets_button(self):
        """
        Clicks on the 'Accept' button after waiting for it to be clickable.
        """
        element = WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.ACCEPT_BUTTON)))
        time.sleep(2)
        element.click()
        logging.info("Clicked on accept terms")

    def add_and_view_my_assets_flow(self):
        """
        Performs the flow of adding an asset to 'My Assets' and then viewing 'My Assets'.
        """
        self.click_on_add_to_my_assets_button()
        self.click_on_accept_to_my_assets_button()
        self.click_on_my_assets_button()

