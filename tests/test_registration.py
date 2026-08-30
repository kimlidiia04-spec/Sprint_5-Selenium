from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from generators import generate_email, generate_password
from locators import *
from tests.constants import BASE_URL

# ПРОВЕРКА УСПЕШНОЙ РЕГИСТРАЦИИ
def test_successful_registration(driver):
    driver.find_element(*personal_account_button).click()
    driver.find_element(*register_link).click()

    email = generate_email()
    password = generate_password()

    driver.find_element(*register_name_input).send_keys("Test User")
    driver.find_element(*register_email_input).send_keys(email)
    driver.find_element(*register_password_input).send_keys(password)
    driver.find_element(*register_button).click()

    WebDriverWait(driver, 10).until(EC.url_to_be(BASE_URL + "login"))

    driver.quit()

# ПРОВЕРКА СООБЩЕНИЯ "НЕКОРРЕКТНЫЙ ПАРОЛЬ"
def test_registration_with_invalid_password(driver):
    driver.find_element(*personal_account_button).click()
    driver.find_element(*register_link).click()

    email = generate_email()

    driver.find_element(*register_name_input).send_keys(email)
    driver.find_element(*register_email_input).send_keys(email)
    driver.find_element(*register_password_input).send_keys("12345")
    driver.find_element(*register_button).click()

    assert driver.find_element(*password_error).text == "Некорректный пароль"

    driver.quit()
    