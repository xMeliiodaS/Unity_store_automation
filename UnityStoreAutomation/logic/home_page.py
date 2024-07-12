import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from logic.base_app_page import BaseAppPage
from logic.utils import Utils


class HomePage(BaseAppPage):
    ASSET_LINK = '//div[@data-test="package-title"]'
    SUB_CATEGORIES = '//a[@class="_1oxj5"]'

    PRICING_BUTTON = '//strong[text() = "Pricing"]'
    FREE_ASSETS_BUTTON = '//span[text() = "Free Assets"]'

    ADD_TO_FAVORITE_ICON = '//button[@class="_2wt5x normal _29YX2"]'
    FAVORITES_BUTTON = '//div[text() = "Favorites"]'
    SAVE_TO_FAVORITE_BUTTON = '//div[text() = "Save"]'

    def __init__(self, driver):
        """
        Initialize the HomePage with a WebDriver instance.

        :param driver: The WebDriver instance to use for browser interactions.
        """
        super().__init__(driver)

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

    def click_on_add_to_favorites_icon(self):
        """
        Clicks on the second "Add to Favorites" icon.

        This method waits for all "Add to Favorites" icons to be present and clicks on the second one.
        """
        WebDriverWait(self._driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, self.ADD_TO_FAVORITE_ICON)))[1].click()

    def click_on_favorites_button(self):
        """
        Clicks on the favorites button.

        This method waits for the favorites button to be present and clicks on it.
        """
        WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.FAVORITES_BUTTON))).click()

    def click_on_save_to_favorites_button(self):
        """
        Clicks on the "Save to Favorites" button.

        This method waits for the "Save to Favorites" button to be present and clicks on it.
        """
        WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.SAVE_TO_FAVORITE_BUTTON))).click()

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
