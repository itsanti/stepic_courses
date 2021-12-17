import math
import time
from fixture_browser import browser
import pathlib


class TestResource:
    def test_page(self, browser: browser):
        link = "http://suninjuly.github.io/file_input.html"
        browser.get(link)

        browser.find_element_by_name("firstname").send_keys("firstname")
        browser.find_element_by_name("lastname").send_keys("lastname")
        browser.find_element_by_name("email").send_keys("email@example.com")

        filename = pathlib.Path('..') / 'data' / 'log.txt'
        browser.find_element_by_name("file").send_keys(filename.resolve().as_posix())

        browser.find_element_by_css_selector('button[type="submit"]').click()

        time.sleep(5)
