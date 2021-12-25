import time


def test_find_add_to_cart_button(browser):
    browser.get('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
    assert browser.find_element_by_css_selector('.btn-add-to-basket')
    time.sleep(10)
