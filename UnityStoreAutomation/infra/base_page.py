class BasePage:
    """
    Base class for all page objects. Contains common methods and attributes.
    """

    # Always get driver
    def __init__(self, driver):
        """
        Initialize the BasePage with a WebDriver instance.

        :param driver: The WebDriver instance to use for browser interactions.
        """
        self._driver = driver

    def refresh_page(self):
        """
        Refresh the current page.
        """
        self._driver.reload()

    def scroll(self, amount_to_scroll):
        """
        Scroll down the current page by 500 pixels.

        :param amount_to_scroll: The scroll amount in pixels.
        """
        self._driver.execute_script(f"window.scrollBy(0, {amount_to_scroll});")
