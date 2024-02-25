import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import url_links


@pytest.fixture()
def browser():
    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.get(url_links.URL)
    yield driver
    driver.quit()

