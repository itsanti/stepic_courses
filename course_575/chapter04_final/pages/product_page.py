from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        btn = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        btn.click()

    def clear_basket(self):
        btn = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        btn.click()

    def should_be_success_message(self):
        msg = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_MSG)
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        assert product_name.text == msg.text, "Product name is not presented"

    def should_be_basket_total_message(self):
        product_price_msg = self.browser.find_element(*ProductPageLocators.PRICE_MSG)
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        assert product_price_msg.text == product_price.text, "Product price is not equaled"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MSG), \
           "Success message is presented, but should not be"

    def should_be_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MSG), \
           "Success message is not disappeared, but should be"
