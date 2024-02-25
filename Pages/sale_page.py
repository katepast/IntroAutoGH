from selenium.webdriver.common.by import By

from Pages.base_page import BasePage


class SalePage(BasePage):
    SALE_MENU_ITEM = (By.ID, "ui-id-8")

    def __int__(self, browser):
        super().__init__(browser)

    def click_sale_btn(self):
        self.click_element(self.SALE_MENU_ITEM)
