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

    def scroll_to_element(self, element):
        """
        Scroll the specified element into view.

        :param element: The WebElement to scroll into view.
        """
        self._driver.execute_script("arguments[0].scrollIntoView(true);", element)

