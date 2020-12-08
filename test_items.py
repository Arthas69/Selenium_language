import time

import pytest

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


class TestLanguage:
    def test_add_basket_button_exists(self, browser):
        browser.get(link)
        # time.sleep(10)
        element = WebDriverWait(browser, 10).until(
            ec.visibility_of_element_located((By.CSS_SELECTOR, '#add_to_basket_form > button'))
        )
        test_attr = element.get_attribute('class')

        assert 'btn-add-to-basket' in test_attr, 'Not the needed button'
