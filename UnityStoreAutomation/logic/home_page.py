from selenium.webdriver.common.by import By
from infra.base_page import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage(BasePage):
    ACCOUNT_BUTTON = '//button[@class="button right-nav-element"]'
    SIGN_IN_BUTTON = '//div[@class="_2zqSQ"]'  # Element won't appear if already signed in

    def __init__(self, driver):
        """
        Initialize the HomePage with a WebDriver instance.

        :param driver: The WebDriver instance to use for browser interactions.
        """
        super().__init__(driver)

    def click_on_account_button(self):
        """
        Click on the account button.

        This method waits for the account button to be present and then clicks on it.
        """
        element = WebDriverWait(self._driver, 5).until(
            EC.presence_of_element_located((By.XPATH, self.ACCOUNT_BUTTON)))
        element.click()

    def click_on_sign_in_button(self):
        """
        Click on the sign-in button.

        This method waits for the sign-in button to be present and then clicks on it.
        If the user already singed up then this button will not be found!
        """
        element = WebDriverWait(self._driver, 5).until(
            EC.presence_of_element_located((By.XPATH, self.SIGN_IN_BUTTON)))
        element.click()
