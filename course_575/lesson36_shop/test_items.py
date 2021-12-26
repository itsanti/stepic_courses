import time
import selenium


def test_find_add_to_cart_button(browser):
    browser.get('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
    add = None
    try:
        add = browser.find_element_by_css_selector('.btn-add-to-basket')
    except selenium.common.exceptions.NoSuchElementException:
        assert add, "no button"
    time.sleep(10)
