"""
This module contains web test cases for the tutorial.
Tests use Selenium WebDriver with Chrome and ChromeDriver.
The fixtures set up and clean up the ChromeDriver instance.
"""

import pytest

from pages import result
from pages import search

@pytest.mark.parametrize('phrase, link', [
    ('panda ramen', 'http://www.pandaramen.pl/'),
    ('umami', 'http://www.restauracjaumami.pl/')])
def test_basic_google_search(browser, phrase, link):

    # Search for the phrase
    search_page = search.GoogleSearchPage(browser)
    search_page.open()
    search_page.search(phrase)

    # Verify that results appear
    result_page = result.GoogleResultPage(browser)
    assert result_page.link_count(link) == 1