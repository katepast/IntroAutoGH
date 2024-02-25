from selenium.common import TimeoutException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, browser: WebDriver):
        self.browser = browser

    def open(self, url):
        return self.browser.get(url)

    def find(self, locator):
        return self.browser.find_element(*locator)

    def click_element(self, locator):
        self.find(locator).click()

    def get_url(self):
        return self.browser.current_url

    def wait_till_element_is_displayed(self, locator, timeout=10):
        wait = WebDriverWait(self.browser, timeout)
        try:
            wait.until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False


