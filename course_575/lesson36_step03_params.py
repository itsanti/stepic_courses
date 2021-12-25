import math
import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from fixture_browser import browser


@pytest.mark.parametrize('page_id', [236895, 236896, 236897, 236898, 236899, 236903, 236904, 236905])
class TestResource:
    def test_page(self, browser: browser, page_id):
        browser.get(f'https://stepik.org/lesson/{page_id}/step/1')
        textarea = WebDriverWait(browser, 5).until(
            EC.presence_of_element_located((By.TAG_NAME, "textarea"))
        )
        textarea.send_keys(str(math.log(int(time.time()))))

        browser.find_element_by_css_selector('button.submit-submission').click()

        feedback = WebDriverWait(browser, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".smart-hints__hint"))
        )

        assert feedback.text == "Correct!"
