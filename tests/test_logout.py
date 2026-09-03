from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import *
from constants import Url

# ВЫХОД ИЗ АККАУНТА
class TestLogOut:

    def test_logout(self, personal_account_driver):
        personal_account_driver.find_element(*logout_button).click()

        personal_account_driver.find_element(*logout_button).click()
        assert WebDriverWait(personal_account_driver, 10).until(EC.url_to_be(Url.BASE_URL + "login"))
