from selenium.webdriver.common.by import By

from Pages.base_page import BasePage
from Pages.sale_page import SalePage


class MainPage(BasePage):
    SALE_MENU_ITEM = (By.ID, "ui-id-8")

    def __int__(self, browser):
        super().__init__(browser)

    def click_sale_btn(self):
        self.wait_till_element_is_displayed(self.SALE_MENU_ITEM)
        self.click_element(self.SALE_MENU_ITEM)
        return SalePage(self.browser)
