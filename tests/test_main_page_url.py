import url_links
from Pages.MainPage import MainPage
import allure


@allure.feature('URL Main page')
def test_open(browser):
    with allure.step('open main page'):
        main_page = MainPage(browser)
    with allure.step('url link equals to the main url link'):
        assert url_links.URL == main_page.get_url(), f"URL is not correspond to {url_links.URL}"

