"""
This module contains GoogleResultPage,
the page object for the Google search result page.
"""

from selenium.webdriver.common.by import By


class GoogleResultPage:

    SEARCH_INPUT = (By.ID, 'search_form_input')

    def __init__(self, browser):
        self.browser = browser

    def link_count(self, link):
        link_selector = (By.CSS_SELECTOR, 'a[href="{}"]'.format(link))
        link_divs = self.browser.find_elements(*link_selector)
        return len(link_divs)
