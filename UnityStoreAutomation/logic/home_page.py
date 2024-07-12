import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from logic.base_app_page import BaseAppPage
from logic.utils import Utils
from selenium.webdriver.support.ui import Select


class HomePage(BaseAppPage):

    ASSET_LINK = '//div[@data-test="package-title"]'
    SUB_CATEGORIES = '//a[@class="_1oxj5"]'

    ASSETS_PRICE_TEXT = '//div[@class="mErEH _223RA"]'
    PRICING_BUTTON = '//strong[text() = "Pricing"]'
    FREE_ASSETS_BUTTON = '//span[text() = "Free Assets"]'
    MIN_PRICE_INPUT = '//input[@type="text" and @value="0"]'
    MAX_PRICE_INPUT = '//input[@type="text" and @value="1500"]'
    SUBMIT_PRICE_BUTTON = '//button[@class="_2ZxFr"]'

    VIEW_RESULT_DROPDOWN_BUTTON = '//div[@class="_1ofYm" and text() = "24"]'
    DROPDOWN_OPTIONS = '//div[@class="_3BlIq" and (text() = "24" or text()="48" or text()="72" or text()="96")]'

    def __init__(self, driver):
        """
        Initialize the HomePage with a WebDriver instance.

        :param driver: The WebDriver instance to use for browser interactions.
        """
        super().__init__(driver)
        try:
            self._min_price_input = WebDriverWait(self._driver, 10).until(
                EC.presence_of_element_located((By.XPATH, self.MIN_PRICE_INPUT)))
            self._max_price_input = WebDriverWait(self._driver, 10).until(
                EC.presence_of_element_located((By.XPATH, self.MAX_PRICE_INPUT)))
            self._view_result_button = WebDriverWait(self._driver, 10).until(
                EC.presence_of_element_located((By.XPATH, self.VIEW_RESULT_DROPDOWN_BUTTON)))

        except NoSuchElementException as e:
            print("Element not found nigga", e)

    def click_on_asset_link(self):
        """
        Clicks on the third asset link.

        This method waits for all asset link elements to be present, scrolls to the third one,
        and clicks on it.
        """
        element = WebDriverWait(self._driver, 8).until(
            EC.presence_of_all_elements_located((By.XPATH, self.ASSET_LINK)))[2]
        self.scroll_to_element(element)
        element.click()

    def click_on_asset_link_by_index(self, index):
        """
        Clicks on an asset link by its index.

        This method waits for all asset link elements to be present, scrolls to the specified index,
        and clicks on it.

        :param index: The index of the asset link to click.
        """
        elements = WebDriverWait(self._driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, f'(//div[@data-test="package-title"])')))
        self.scroll_to_element(elements[index])
        elements[index].click()

    def click_on_category_by_name(self, name):
        """
        Clicks on a category by its name.

        This method waits for the category element to be present and clicks on it.

        :param name: The name of the category to click.
        """
        element = WebDriverWait(self._driver, 5).until(
            EC.presence_of_element_located((By.XPATH, f'//a[text()="{name}"]')))
        element.click()

    def get_random_category_text(self):
        """
        Returns the text of a random sub-category.

        This method waits for all sub-category elements to be present, selects a random one,
        and returns its text.
        """
        random_index = Utils.generate_random_number() - 1
        elements = WebDriverWait(self._driver, 5).until(
            EC.presence_of_all_elements_located((By.XPATH, self.SUB_CATEGORIES)))
        return elements[random_index].text

    def click_on_pricing_button(self):
        """
        Clicks on the pricing button.

        This method waits for the pricing button to be clickable, scrolls to it,
        and clicks on it.
        """
        element = WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.PRICING_BUTTON)))
        self.scroll_to_element(element)
        element.click()

    def click_on_free_assets_button(self):
        """
        Clicks on the free assets button.

        This method waits for the free assets button to be clickable, clicks on it,
        and waits for the page to load.
        """
        element = WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.FREE_ASSETS_BUTTON)))
        element.click()
        time.sleep(4)

    def free_asset_navigation_flow(self, asset_index):
        """
        Navigates through the pricing section, then the free assets section,
        and finally clicks on an asset link by index.

        This method performs a series of clicks to navigate through the pricing section,
        then the free assets section, and finally clicks on an asset link specified by the index.

        :param asset_index: The index of the asset link to be clicked.
        """
        self.click_on_pricing_button()
        self.click_on_free_assets_button()
        self.click_on_asset_link_by_index(asset_index)

    def assets_price_list(self):
        return WebDriverWait(self._driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, self.ASSETS_PRICE_TEXT)))

    def click_on_submit_price_button(self):
        element = WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.SUBMIT_PRICE_BUTTON)))
        self.scroll_to_element(element)
        element.click()

    def fill_min_price_input(self, min_price):
        self._min_price_input.clear()
        self._min_price_input.send_keys(min_price)

    def fill_max_price_input(self, max_price):
        self._max_price_input.clear()
        self._max_price_input.send_keys(max_price)

    def get_assets_price_list(self):
        """
        Fetches the list of asset prices from the page.
        """
        time.sleep(1)
        asset_elements = self.assets_price_list()
        asset_prices = [element.text for element in asset_elements]
        return asset_prices

    def process_and_sort_asset_prices(self):
        """
        Processes and sorts the list of asset prices.
        """
        assets_price_list = self.get_assets_price_list()
        return sorted(float(price.replace('$', '').replace(',', ''))
                      for price in assets_price_list)

    def fill_max_min_price_inputs_flow(self, max_price, min_price):
        self.fill_max_price_input(max_price)
        self.fill_min_price_input(min_price)
        self.click_on_submit_price_button()

    def click_on_view_results_dropdown_button(self):
        self._view_result_button.click()

    def get_dropdown_options(self):
        return WebDriverWait(self._driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, self.DROPDOWN_OPTIONS)))

    def select_from_dropdown_by_value(self, value):
        """
        Selects an option from the dropdown menu by its value attribute.

        :param value: The value attribute of the option to select.
        """
        # Get all dropdown options
        options = self.get_dropdown_options()

        # Iterate through options and click on the one with matching text
        for option in options:
            if int(option.text) == value:
                self.scroll_to_element(option)
                option.click()
                return

        # Handle case when option with specified value is not found
        raise ValueError(f"Option with value '{value}' not found in dropdown.")

    def get_current_assets_count_in_page(self):
        return len(WebDriverWait(self._driver, 8).until(
            EC.presence_of_all_elements_located((By.XPATH, self.ASSET_LINK))))