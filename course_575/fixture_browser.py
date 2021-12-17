import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture()
def browser():
    chrome_options = Options()
    chrome_options.add_argument("--window-size=1600,900")
    chrome_options.add_argument("--user-data-dir=K:\\chrome_profiles\\qa_chrome")
    chrome_options.add_argument("--disable-extensions")
    driver = webdriver.Chrome('../bin/chromedriver96.exe', options=chrome_options)
    yield driver
    driver.quit()
