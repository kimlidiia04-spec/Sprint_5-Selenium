from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import *
from constants import Url

# ВЫХОД ИЗ АККАУНТА
class TestLogOut:

    def test_logout(self, logged_in_driver):
        logged_in_driver.find_element(*personal_account_button).click()
        assert WebDriverWait(logged_in_driver, 10).until(EC.url_to_be(Url.BASE_URL + "account/profile"))

        logged_in_driver.find_element(*logout_button).click()
        assert WebDriverWait(logged_in_driver, 10).until(EC.url_to_be(Url.BASE_URL + "login"))
