from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    LOGOUT_LINK = (By.CSS_SELECTOR, "#logout_link")
    BASKET_LINK = (By.CSS_SELECTOR, "header .basket-mini a.btn-default[href*='basket']")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators:
    pass


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REG_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REG_PASS = (By.CSS_SELECTOR, "#id_registration-password1")
    REG_PASS_CONFIRM = (By.CSS_SELECTOR, "#id_registration-password2")
    REG_SUBMIT = (By.CSS_SELECTOR, "button[name='registration_submit']")


class BasketPageLocators:
    CONTENT = (By.CSS_SELECTOR, "#content_inner")
    ITEM_QUANTITY = (By.CSS_SELECTOR, "#id_form-0-quantity")
    ITEM_UPDATE = (By.CSS_SELECTOR, ".checkout-quantity button[type='submit']")


class ProductPageLocators:
    BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    SUCCESS_MSG = (By.CSS_SELECTOR, "#messages .alert:first-child .alertinner")
    PRICE_MSG = (By.CSS_SELECTOR, "#messages .alert:last-child .alertinner p strong")
    PRODUCT_NAME_MSG = (By.CSS_SELECTOR, "#messages .alert:first-child .alertinner strong")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
