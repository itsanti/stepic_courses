import math
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from fixture_browser import browser


class TestResource:
    def test_page(self, browser: browser):
        browser.get('http://suninjuly.github.io/explicit_wait2.html')

        WebDriverWait(browser, 12).until(
            EC.text_to_be_present_in_element((By.ID, "price"), '100')
        )

        browser.find_element_by_id("book").click()

        self._solve_quiz(browser)

        time.sleep(1)

    def _solve_quiz(self, browser):
        f = lambda x: math.log(abs(12 * math.sin(x)))
        input_value = int(browser.find_element_by_id("input_value").text)
        browser.find_element_by_id("answer").send_keys(str(f(input_value)))
        browser.find_element_by_css_selector('button[type="submit"]').click()
        print('\nAnswer to Stepik quiz:', browser.switch_to.alert.text.split(' ')[-1])
