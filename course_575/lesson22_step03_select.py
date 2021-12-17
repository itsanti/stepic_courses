from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
import time

try:
    chrome_options = Options()
    chrome_options.add_argument("--window-size=1600,900")
    chrome_options.add_argument("--user-data-dir=K:\\chrome_profiles\\qa_chrome")
    chrome_options.add_argument("--disable-extensions")
    browser = webdriver.Chrome('../bin/chromedriver96.exe', chrome_options=chrome_options)

    link = "http://suninjuly.github.io/selects2.html"
    browser.get(link)

    num1 = int(browser.find_element_by_id("num1").text)
    num2 = int(browser.find_element_by_id("num2").text)

    select = Select(browser.find_element_by_class_name("custom-select"))
    select.select_by_value(str(num1 + num2))

    assert select.first_selected_option.text == str(num1 + num2)

    button = browser.find_element_by_css_selector('[type="submit"]')
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
