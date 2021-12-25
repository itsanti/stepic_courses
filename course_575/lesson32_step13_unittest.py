import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class TestRegistration(unittest.TestCase):
    def setUp(self) -> None:
        chrome_options = Options()
        chrome_options.add_argument("--window-size=1600,900")
        chrome_options.add_argument("--user-data-dir=K:\\chrome_profiles\\qa_chrome")
        chrome_options.add_argument("--disable-extensions")
        self.browser = webdriver.Chrome('../bin/chromedriver96.exe', options=chrome_options)

    def tearDown(self) -> None:
        self.browser.close()

    def test_registration1(self):
        browser = self.browser
        link = "http://suninjuly.github.io/registration%s.html"
        browser.get(link % 1)
        input1 = browser.find_element_by_xpath('//label[contains(text(), "First")]/following-sibling::input')
        input1.send_keys('First name')
        input2 = browser.find_element_by_xpath('//label[contains(text(), "Last")]/following-sibling::input')
        input2.send_keys('Last name')
        input3 = browser.find_element_by_xpath('//label[contains(text(), "Email")]/following-sibling::input')
        input3.send_keys('Email')
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

    def test_registration2(self):
        browser = self.browser
        link = "http://suninjuly.github.io/registration%s.html"
        browser.get(link % 2)
        input1 = browser.find_element_by_xpath('//label[contains(text(), "First")]/following-sibling::input')
        input1.send_keys('First name')
        input2 = browser.find_element_by_xpath('//label[contains(text(), "Last")]/following-sibling::input')
        input2.send_keys('Last name')


if __name__ == "__main__":
    unittest.main()
