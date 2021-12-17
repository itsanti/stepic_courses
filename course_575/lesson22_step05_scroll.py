import math
import time
from fixture_browser import browser


class TestResource:
    def test_page(self, browser: browser):
        link = "https://SunInJuly.github.io/execute_script.html"
        browser.get(link)

        input_value = browser.find_element_by_id("input_value")
        value = self.math(int(input_value.text))

        answer = browser.find_element_by_id("answer")
        answer.send_keys(str(value))

        button = browser.find_element_by_tag_name("button")
        button.location_once_scrolled_into_view

        browser.find_element_by_id("robotCheckbox").click()
        browser.find_element_by_id("robotsRule").click()

        button.click()
        time.sleep(5)

    def math(self, x):
        return math.log(abs(12 * math.sin(x)))