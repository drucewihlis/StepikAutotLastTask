from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def click_add_to_basket(self):
        btn_add_to_basket = self.browser.find_element(*ProductPageLocators.BTN_ADD_TO_BASKET)
        btn_add_to_basket.click()

    def should_be_bookname_in_notify(self, browser):
        book_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME).text
        WebDriverWait(browser, 5).until(
            EC.text_to_be_present_in_element((ProductPageLocators.NOTIFY_ADDED_TO_BASKET), book_name))
        assert book_name in self.browser.find_element(*ProductPageLocators.NOTIFY_ADDED_TO_BASKET).text

    def should_be_price_in_notify(self, browser):
        book_price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text
        WebDriverWait(browser, 5).until(
            EC.text_to_be_present_in_element((ProductPageLocators.NOTIFY_BASKET_TOTAL), book_price))
        assert book_price in self.browser.find_element(*ProductPageLocators.NOTIFY_BASKET_TOTAL).text
