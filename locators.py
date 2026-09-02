from selenium.webdriver.common.by import By

#ПЕРЕХОД_В_ЛК И ССЫЛКА НА ВХОД
personal_account_button = ("xpath", "//p[text()='Личный Кабинет']") # кнопка Личный кабинет
login_link = ("xpath", "//a[@href='/login']") # ссылка Войти на форму входа в лк

#БЛОК_РЕГИСТРАЦИЯ
register_link = ("xpath", "//a[@href='/register']") # ссылка на страницу Регистрации
register_name_input = ("xpath", "(//input[@name='name'])[1]") # поле ввода Имя
register_email_input = ("xpath", "(//input[@name='name'])[2]") # поле ввода Электронной почты 
register_password_input = ("xpath", "//input[@name='Пароль']") # поле ввода Пароля
password_error = ("xpath", "//p[text()='Некорректный пароль']") # сообщение Некоректный пароль

#БЛОК_ВХОД 
login_button = ("xpath", "//button[text()='Войти в аккаунт']") # кнопка Войти в аккаунт на главной странице
register_button =("xpath", "//button[text()='Зарегистрироваться']") # кнопка Зарегистрироваться
restore_password_button = ("xpath", "//button[text()='Восстановить']") # кнопка Восстановить
restore_password_link = ("xpath", "//a[@href='/forgot-password']")  # ссылка на странцу восстановления

#ПЕРЕХОД_ИЗ_ЛК_В_КОНСТРУКТОР И ЛОГО
constructor_button = ("xpath", "//p[text()='Конструктор']") # кнопка Конструктор
logo_button = (By.XPATH, "//a[@href='/']") # кнопка Лого

#ВХОД И ВЫХОД_ИЗ_АККАУНТА
login_email_input = ("xpath", "//input[@name='name']") # поле ввода email
login_password_input = ("xpath", "//input[@name='Пароль']") # поле ввода password
login_submit_button = ("xpath", "//button[text()='Войти']") # кнопка Войти в ворме ввода данных
logout_button = ("xpath", "//button[text()='Выход']") # кнопка Выход

#РАЗДЕЛ_КОНСТРУКТОР
buns_tab = ("xpath", "//span[text()='Булки']") # раздел Булки
sauces_tab = ("xpath", "//span[text()='Соусы']") # раздел Соусы
fillings_tab = ("xpath", "//span[text()='Начинки']") # Раздел Начинки

buns_tab_active = ("xpath", "//span[text()='Булки']/parent::*[contains(@class, 'tab_tab_type_current')]")
sauces_tab_active = ("xpath", "//span[text()='Соусы']/parent::*[contains(@class, 'tab_tab_type_current')]")
fillings_tab_active = ("xpath", "//span[text()='Начинки']/parent::*[contains(@class, 'tab_tab_type_current')]")
