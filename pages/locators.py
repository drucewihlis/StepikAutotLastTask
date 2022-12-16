from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    BTN_ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    NOTIFY_ADDED_TO_BASKET = (By.CSS_SELECTOR, "#messages .alert:nth-child(1)")
    NOTIFY_BASKET_TOTAL = (By.CSS_SELECTOR, "#messages .alert:nth-child(3)")
    BOOK_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
