from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import *
from constants import Url

class TestConstructor:
    # ПЕРЕХОД ПО КНОПКЕ "ЛИЧНЫЙ КАБИНЕТ"
    def test_personal_account(self, logged_in_driver):
        logged_in_driver.find_element(*personal_account_button).click()

        assert WebDriverWait(logged_in_driver, 10).until(EC.url_to_be(Url.BASE_URL+"account/profile"))

    # ПЕРЕХОД ИЗ ЛИЧНОГО КАБИНЕТА В КОНСТРУКТОР
    def test_constructor_from_personal_account(self, personal_account_driver):
        personal_account_driver.find_element(*constructor_button).click()
        assert WebDriverWait(personal_account_driver, 10).until(EC.url_to_be(Url.BASE_URL))


    # ПЕРЕХОД НА ГЛАВНУЮ СТРАНИЦУ ПО ЛОГО
    def test_logo_from_personal_account(self, personal_account_driver):
        personal_account_driver.find_element(*logo_button).click()
        assert WebDriverWait(personal_account_driver, 10).until(EC.url_to_be(Url.BASE_URL))

    # РАЗДЕЛ "БУЛКИ" В КОНСТРУКТОРЕ
    def test_buns_tab(self, logged_in_driver):
        logged_in_driver.find_element(*sauces_tab).click()
        buns = WebDriverWait(logged_in_driver, 10).until(EC.element_to_be_clickable(buns_tab))
        buns.click()
        assert WebDriverWait(logged_in_driver, 10).until(EC.visibility_of_element_located(buns_tab_active))

    # РАЗДЕЛ "СОУСЫ" В КОНСТРУКТОРЕ
    def test_sauces_tab(self, logged_in_driver):
        sauces = WebDriverWait(logged_in_driver, 10).until(EC.element_to_be_clickable(sauces_tab))
        sauces.click()
        assert WebDriverWait(logged_in_driver, 10).until(EC.visibility_of_element_located(sauces_tab_active))

    # РАЗДЕЛ "НАЧИНКИ" В КОНСТРУКТОРЕ
    def test_fillings_tab(self, logged_in_driver):
        fillings = WebDriverWait(logged_in_driver, 10).until(EC.element_to_be_clickable(fillings_tab))
        fillings.click()
        assert WebDriverWait(logged_in_driver, 10).until(EC.visibility_of_element_located(fillings_tab_active))