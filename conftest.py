from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

from locators import *

BASE_URL = "https://stellarburgers.education-services.ru/"


def get_driver(browser_name):
    if browser_name == "chrome":
        return webdriver.Chrome()
    elif browser_name == "firefox":
        return webdriver.Firefox()
    else:
        raise ValueError(f"Неизвестный браузер: {browser_name}")


@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    driver = get_driver(request.param)
    driver.get(BASE_URL)
    return driver


@pytest.fixture(params=["chrome", "firefox"])
def logged_in_driver(request):
    driver = get_driver(request.param)
    wait = WebDriverWait(driver, 10)

    driver.get(BASE_URL)
    driver.find_element(*personal_account_button).click()

    driver.find_element(*login_email_input).send_keys("lidia_kim_51_123@mail.ru")
    driver.find_element(*login_password_input).send_keys("1234567890")
    driver.find_element(*login_submit_button).click()

    wait.until(EC.url_to_be(BASE_URL))

    return driver