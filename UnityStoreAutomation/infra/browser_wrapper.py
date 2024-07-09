from selenium import webdriver
from infra.config_provider import ConfigProvider
from selenium import common as c
import undetected_chromedriver as uc


class BrowserWrapper:

    def __init__(self):
        self._driver = None
        self.config = ConfigProvider().load_config_json()

    def get_driver(self, url):
        try:
            options = uc.ChromeOptions()
            options.add_argument("--disable-blink-features=AutomationControlled")
            if self.config["browser"] == "Chrome":
                self._driver = uc.Chrome(options=options)
            elif self.config["browser"] == "Firefox":
                self._driver = webdriver.Firefox()
            else:
                print("Browser does not exist")

            self._driver.get(url)
            return self._driver
        except c.WebDriverException as e:
            print("Could not find web driver:", e)

    def close_browser(self):
        self._driver.quit()
        print("Test done")