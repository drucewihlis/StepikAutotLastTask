from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException, TimeoutException

from .base_page import BasePage
from .locators import *

class BasketPage(BasePage):

    def should_be_no_items_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS)

    def should_be_text_empty_basket(self, browser):
        assert WebDriverWait(browser, 5).until(
            EC.text_to_be_present_in_element((BasketPageLocators.NOTIFY_EMPTY_BASKET), "Your basket is empty.")), \
            "Wrong text about empty basket"