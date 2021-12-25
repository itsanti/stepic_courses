import math
import time
from fixture_browser import browser


class TestResource:
    def test_page(self, browser: browser):
        browser.get('http://suninjuly.github.io/redirect_accept.html')

        browser.find_element_by_css_selector(".trollface").click()
        browser.switch_to.window(browser.window_handles[1])

        x = int(browser.find_element_by_id("input_value").text)
        result = TestResource.solve(x)

        browser.find_element_by_id("answer").send_keys(str(result))
        browser.find_element_by_css_selector('button[type="submit"]').click()

        time.sleep(5)

    @staticmethod
    def solve(x):
        # ln(abs(12*sin(x)))
        return math.log(abs(12 * math.sin(x)))
