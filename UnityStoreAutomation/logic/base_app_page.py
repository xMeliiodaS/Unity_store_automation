import logging
import time
from selenium.webdriver.common.by import By
from infra.base_page import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


class BaseAppPage(BasePage):
    # ------------------Locator related to the cookies------------------
    CLOSE_COOKIES_TAB = '//div[@id="onetrust-close-btn-container"]//button[@aria-label="Close"]'

    # ------------------Locators related to the header------------------
    ACCOUNT_BUTTON = '//button[@class="button right-nav-element"]'
    SIGN_IN_BUTTON = '//div[@class="_2zqSQ"]'
    MY_ASSETS_BUTTON = '//button[@class="_3-jib assets right-nav-element"]'
    SAVED_ASSETS_BUTTON = '//button[@class="_3-jib favs right-nav-element"]'
    CART_BUTTON = '//button[contains(@class, "cartMini")]'
    PERSONAL_SETTINGS = '//div[text() = "Personal Settings"]'
    LOGOUT = '//div[text() ="Sign Out"]'

    # ------------------Locators related to the cart popup------------------
    VIEW_CART_BUTTON = '//button[@label="View cart"]'
    REMOVE_ASSET_FROM_CART_BUTTON = '//button[@label="Remove"]'

    def __init__(self, driver):
        """
        Initialize the HomePage with a WebDriver instance.

        :param driver: The WebDriver instance to use for browser interactions.
        """
        super().__init__(driver)

    def click_on_close_cookies_button(self):
        """
        This method waits for the cookies close button to be clickable and then clicks on it.
        """
        WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.CLOSE_COOKIES_TAB))).click()

    def click_on_account_button(self):
        """
        This method waits for the account button to be clickable and then clicks on it.
        """
        element = WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.ACCOUNT_BUTTON)))
        element.click()

    def click_on_sign_in_button(self):
        """
        This method waits for the sign-in button to be clickable and then clicks on it.
        If the user is already signed in, this button will not be found.
        """
        try:
            WebDriverWait(self._driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, self.SIGN_IN_BUTTON))).click()
        except NoSuchElementException:
            print("The use ris already signed in, hence there is no such a button")

    def click_on_my_assets_button(self):
        """
        This method waits for the "My Assets" button to be clickable and then clicks on it.
        """
        WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.MY_ASSETS_BUTTON))).click()
        logging.info("Clicked on 'My Asset' tab")

    def click_on_saved_assets_button(self):
        """
        This method waits for the "Saved Assets" button to be clickable and then clicks on it.
        """
        WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.SAVED_ASSETS_BUTTON))).click()

    def click_on_cart_button(self):
        """
        Clicks on the cart button to view the cart.

        This method waits for the cart button to be clickable and then clicks on it.
        """
        WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.CART_BUTTON))).click()

    def click_view_cart_button(self):
        """
        Clicks on the view cart button to go to the cart page.

        This method waits for the view cart button to be clickable and then clicks on it.
        """
        WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.VIEW_CART_BUTTON))).click()
        logging.info("View cart")

    def click_remove_all_assets_from_cart_button(self):
        """
        This method waits for the remove asset button to be clickable and then clicks on it.
        """
        elements = WebDriverWait(self._driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, self.REMOVE_ASSET_FROM_CART_BUTTON)))
        time.sleep(3)
        for element in elements:
            element.click()

    def click_on_personal_settings_button(self):
        """
        This method waits for the personal settings button to be clickable and
         then clicks on it.
        """
        WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.PERSONAL_SETTINGS))).click()
        logging.info("Clicked on the personal settings button")

    def is_logout_displayed(self):
        """
        Checks if the logout button is displayed.

        This method waits for a short period and then checks if the
         logout button is present and displayed.
        """
        time.sleep(1)
        return WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.LOGOUT))).is_displayed()
