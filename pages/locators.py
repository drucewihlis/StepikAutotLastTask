from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini .btn")

class BasketPageLocators():
    NOTIFY_EMPTY_BASKET = (By.CSS_SELECTOR, "#content_inner")
    BASKET_ITEMS = (By.CSS_SELECTOR, ".basket-items")

class MainPageLocators():
    pass
class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    BTN_ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    NOTIFY_ADDED_TO_BASKET = (By.CSS_SELECTOR, "#messages .alert:nth-child(1) strong")
    NOTIFY_BASKET_TOTAL = (By.CSS_SELECTOR, "#messages .alert:nth-child(3) p strong")
    BOOK_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    BOOK_NAME = (By.CSS_SELECTOR, ".product_main h1")
