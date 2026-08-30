from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import *
from tests.constants import BASE_URL

# ВЫХОД ИЗ АККАУНТА
def test_logout(logged_in_driver):
    logged_in_driver.find_element(*personal_account_button).click()
    WebDriverWait(logged_in_driver, 10).until(EC.url_to_be(BASE_URL + "account/profile"))

    logged_in_driver.find_element(*logout_button).click()
    WebDriverWait(logged_in_driver, 10).until(EC.url_to_be(BASE_URL + "login"))

    logged_in_driver.quit()
    