from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import *
from tests.constants import BASE_URL

# ПЕРЕХОД ПО КНОПКЕ "ЛИЧНЫЙ КАБИНЕТ"
def test_personal_account(logged_in_driver):
    logged_in_driver.find_element(*personal_account_button).click()

    WebDriverWait(logged_in_driver, 10).until(EC.url_to_be(BASE_URL + "account/profile"))

    logged_in_driver.quit()

# ПЕРЕХОД ИЗ ЛИЧНОГО КАБИНЕТА В КОНСТРУКТОР
def test_constructor_from_personal_account(logged_in_driver):
    logged_in_driver.find_element(*personal_account_button).click()
    WebDriverWait(logged_in_driver, 10).until(EC.url_to_be(BASE_URL + "account/profile"))

    logged_in_driver.find_element(*constructor_button).click()
    WebDriverWait(logged_in_driver, 10).until(EC.url_to_be(BASE_URL))

    logged_in_driver.quit()
    
# ПЕРЕХОД НА ГЛАВНУЮ СТРАНИЦУ ПО ЛОГО
def test_logo_from_personal_account(logged_in_driver):
    logged_in_driver.find_element(*personal_account_button).click()
    WebDriverWait(logged_in_driver, 10).until(EC.url_to_be(BASE_URL + "account/profile"))

    logged_in_driver.find_element(*logo_button).click()
    WebDriverWait(logged_in_driver, 10).until(EC.url_to_be(BASE_URL))

    logged_in_driver.quit()

# РАЗДЕЛ "БУЛКИ" В КОНСТРУКТОРЕ
def test_buns_tab(logged_in_driver):
    buns = WebDriverWait(logged_in_driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//span[text()='Булки']/parent::*")))

    assert buns.is_displayed()

    logged_in_driver.quit()

# РАЗДЕЛ "СОУСЫ" В КОНСТРУКТОРЕ
def test_sauces_tab(logged_in_driver):
    sauces = WebDriverWait(logged_in_driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Соусы']/parent::*")))
    sauces.click()

    assert sauces.is_displayed()

    logged_in_driver.quit()

# РАЗДЕЛ "НАЧИНКИ" В КОНСТРУКТОРЕ
def test_fillings_tab(logged_in_driver):
    fillings = WebDriverWait(logged_in_driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Начинки']/parent::*")))
    fillings.click()

    assert fillings.is_displayed()

    logged_in_driver.quit()
