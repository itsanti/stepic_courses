import time
from fixture_browser import browser


class TestResource:
    def test_page(self, browser: browser):
        browser.get('http://www.google.com/xhtml');
        search_box = browser.find_element_by_name('q')
        search_box.send_keys('давай я поищу за тебя')
        time.sleep(2)
        search_box.submit()
