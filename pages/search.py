"""
This module contains GoogleSearchPage,
the page object for the Google search page.
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class GoogleSearchPage:

    URL = 'https://www.google.com'

    SEARCH_INPUT = (By.CSS_SELECTOR, 'input[type="text"]')
    CONFIRM_BUTTON = (By.XPATH, '//button/div[contains(., "Zgadzam się")]')

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.get(self.URL)
        self.browser.find_element(*self.CONFIRM_BUTTON).click()

    def search(self, text):
        search_input = self.browser.find_element(*self.SEARCH_INPUT)
        search_input.send_keys(text + Keys.RETURN)