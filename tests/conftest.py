from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

from locators import *
from constants import Url, UserData


@pytest.fixture(params=["chrome", "firefox"])
def get_driver(request):
    browser_name = request.param

    if browser_name == "chrome":
        driver = webdriver.Chrome()
    elif browser_name == "firefox":
        driver = webdriver.Firefox()
    else:
        raise ValueError(f"Неизвестный браузер: {browser_name}")

    yield driver
    driver.quit()

@pytest.fixture
def driver(get_driver):
    get_driver.get(Url.BASE_URL)
    return get_driver

@pytest.fixture
def logged_in_driver(get_driver):
    wait = WebDriverWait(get_driver, 10)

    get_driver.get(Url.BASE_URL)
    get_driver.find_element(*personal_account_button).click()

    get_driver.find_element(*login_email_input).send_keys(UserData.LOGIN_EMAIL)
    get_driver.find_element(*login_password_input).send_keys(UserData.LOGIN_PASSWORD)
    get_driver.find_element(*login_submit_button).click()

    wait.until(EC.url_to_be(Url.BASE_URL))

    return get_driver