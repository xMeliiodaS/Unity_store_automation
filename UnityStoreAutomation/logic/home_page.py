import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from logic.base_app_page import BaseAppPage
from logic.utils import Utils


class HomePage(BaseAppPage):
    ASSET_LINK = '//div[@data-test="package-title"]'
    SUB_CATEGORIES = '//a[@class="_1oxj5"]'
    SUB_CATEGORIESs = '//a[@class="_1oxj5"]'

    PRICING_BUTTON = '//strong[text() = "Pricing"]'
    FREE_ASSETS_BUTTON = '//span[text() = "Free Assets"]'

    ADD_TO_FAVORITE_ICON = '//button[@class="_2wt5x normal _29YX2"]'
    FAVORITES_BUTTON = '//div[text() = "Favorites"]'
    SAVE_TO_FAVORITE_BUTTON = '//div[text() = "Save"]'

    def __init__(self, driver):
        super().__init__(driver)

    def click_on_asset_link(self):
        """
        Click on the asset link.
        """
        element = WebDriverWait(self._driver, 8).until(
            EC.presence_of_all_elements_located((By.XPATH, self.ASSET_LINK)))[2]
        self.scroll_to_element(element)
        element.click()

    def click_on_asset_link_by_index(self, index):
        """
        Click on the asset link.
        """
        elements = WebDriverWait(self._driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, f'(//div[@data-test="package-title"])')))
        self.scroll_to_element(elements[index])
        elements[index].click()

    def click_on_category_by_name(self, name):
        """
        Clicks on a random category and returns its name.
        """
        element = WebDriverWait(self._driver, 5).until(
            EC.presence_of_element_located((By.XPATH, f'//a[text()="{name}"]')))
        element.click()

    def get_random_category_text(self):
        random_index = Utils.generate_random_number() - 1
        elements = WebDriverWait(self._driver, 5).until(
            EC.presence_of_all_elements_located((By.XPATH, self.SUB_CATEGORIES)))
        return elements[random_index].text

    def click_on_pricing_button(self):
        """
        Clicks on a random category and returns its name.
        """
        element = WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.PRICING_BUTTON)))
        self.scroll_to_element(element)
        element.click()

    def click_on_free_assets_button(self):
        """
        Clicks on a random category and returns its name.
        """
        element = WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.FREE_ASSETS_BUTTON)))
        element.click()
        time.sleep(4)

    def click_on_add_to_favorites_icon(self):
        """
        Clicks on a random category and returns its name.
        """
        WebDriverWait(self._driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, self.ADD_TO_FAVORITE_ICON)))[1].click()

    def click_on_favorites_button(self):
        """
        Clicks on a random category and returns its name.
        """
        WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.FAVORITES_BUTTON))).click()

    def click_on_save_to_favorites_button(self):
        """
        Clicks on a random category and returns its name.
        """
        WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.SAVE_TO_FAVORITE_BUTTON))).click()

    def free_asset_navigation_flow(self, asset_index):
        """
        Navigates through the pricing section, then the free assets section,
        and finally clicks on an asset link by index.

        :param asset_index: The index of the asset link to be clicked.
        """
        self.click_on_pricing_button()
        self.click_on_free_assets_button()
        self.click_on_asset_link_by_index(asset_index)
