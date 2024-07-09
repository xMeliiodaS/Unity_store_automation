class BasePage:

    # Always get driver
    def __init__(self, driver):
        self._driver = driver

    def refresh_page(self):
        self._driver.reload()

    def scroll(self):
        self._driver.execute_script("window.scrollBy(0, 500);")