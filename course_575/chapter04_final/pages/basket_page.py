from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def is_clear(self):
        content = self.browser.find_element(*BasketPageLocators.CONTENT)
        assert 'basket is empty' in content.text, "Basket is not clear, but should be"

    def clear_basket(self):
        content = self.browser.find_element(*BasketPageLocators.CONTENT)
        if 'basket is empty' not in content.text:
            iq = self.browser.find_element(*BasketPageLocators.ITEM_QUANTITY)
            iq.clear()
            iq.send_keys('0')
            self.browser.find_element(*BasketPageLocators.ITEM_UPDATE).click()
