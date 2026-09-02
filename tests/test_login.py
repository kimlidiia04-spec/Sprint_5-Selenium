from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import *
from constants import Url, UserData

# КНОПКА "ВОЙТИ В АККАУНТ" С ГЛАВНОЙ СТРАНИЦЫ
def test_login_from_main_page(driver):
    driver.find_element(*login_button).click()

    driver.find_element(*login_email_input).send_keys(UserData.LOGIN_EMAIL)
    driver.find_element(*login_password_input).send_keys(UserData.LOGIN_PASSWORD)
    driver.find_element(*login_submit_button).click()

    assert WebDriverWait(driver, 10).until(EC.url_to_be(Url.BASE_URL))

# ВХОД ЧЕРЕЗ КНОПКУ "ЛИЧНЫЙ КАБИНЕТ"
def test_login_from_personal_account(driver):
    driver.find_element(*personal_account_button).click()

    driver.find_element(*login_email_input).send_keys(UserData.LOGIN_EMAIL)
    driver.find_element(*login_password_input).send_keys(UserData.LOGIN_PASSWORD)
    driver.find_element(*login_submit_button).click()

    assert WebDriverWait(driver, 10).until(EC.url_to_be(Url.BASE_URL))

# ВХОД ПО ССЫЛКЕ "ВОЙТИ" В ФОРМЕ РЕГИСТРАЦИИ
def test_login_from_registration(driver):
    driver.find_element(*personal_account_button).click()
    driver.find_element(*register_link).click()
    driver.find_element(*login_link).click()

    driver.find_element(*login_email_input).send_keys(UserData.LOGIN_EMAIL)
    driver.find_element(*login_password_input).send_keys(UserData.LOGIN_PASSWORD)
    driver.find_element(*login_submit_button).click()

    assert WebDriverWait(driver, 10).until(EC.url_to_be(Url.BASE_URL))


# ВХОД ПО ССЫЛКЕ "ВОЙТИ" В ФОРМЕ ВОССТАНОВЛЕНИЯ ПАРОЛЯ
def test_login_from_password_recovery(driver):
    driver.find_element(*personal_account_button).click()
    driver.find_element(*restore_password_link).click()
    driver.find_element(*login_link).click()

    driver.find_element(*login_email_input).send_keys(UserData.LOGIN_EMAIL)
    driver.find_element(*login_password_input).send_keys(UserData.LOGIN_PASSWORD)
    driver.find_element(*login_submit_button).click()

    assert WebDriverWait(driver, 10).until(EC.url_to_be(Url.BASE_URL))
