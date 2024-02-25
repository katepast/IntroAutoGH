import allure
import url_links
from Pages.MainPage import MainPage


@allure.feature('Sale button')
def test_sale_click_btn(browser):
    with allure.step('click on sale button'):
        main_page = MainPage(browser)
        sale_page = main_page.click_sale_btn()
    with allure.step('verify url link equals to sale.html'):
        assert url_links.SALE_LINK == sale_page.get_url(), f"URL is not correspond to {url_links.SALE_LINK}"
