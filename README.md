Автотесты на Selenium для Stellar Burgers

Автоматизированные UI-тесты для сайта Stellar Burgers(https://stellarburgers.education-services.ru/), 
написанные на Python с использованием Selenium и pytest.

Что протестировано:

Регистрация — успешная регистрация нового пользователя, проверка ошибки при вводе некорректного пароля.

Вход в аккаунт — вход через кнопку «Войти в аккаунт» на главной, через «Личный кабинет», через форму регистрации и через форму восстановления пароля.

Навигация — переход в личный кабинет, переход из личного кабинета в конструктор (по кнопке и по логотипу), переключение вкладок «Булки» / «Соусы» / «Начинки» в конструкторе.

Выход из аккаунта — выход по кнопке «Выйти» в личном кабинете.

-Каждый тест автономен: открывает браузер, выполняет проверку и закрывает браузер driver.quit().
-Логин и пароль для регистрации генерируются автоматически generators.py, чтобы избежать конфликта с уже существующими в системе почтами.
-Тесты, требующие авторизации, используют фикстуру logged_in_driver, которая выполняет вход перед стартом теста.

Всего 13 тестов для браузеров Chrome и Firefox. 

Все тесты пройдены в Google Chrome.
При запуске в Mozilla Firefox один тест (`test_constructor_from_personal_account`) завершился с ошибкой.

tests/test_constructor.py::test_personal_account[chrome] PASSED [  3%]
tests/test_constructor.py::test_personal_account[firefox] PASSED [  7%]
tests/test_constructor.py::test_constructor_from_personal_account[chrome] PASSED [ 11%]
*** tests/test_constructor.py::test_constructor_from_personal_account[firefox] FAILED [ 15%] ***
tests/test_constructor.py::test_logo_from_personal_account[chrome] PASSED [ 19%]
tests/test_constructor.py::test_logo_from_personal_account[firefox] PASSED [ 23%]
tests/test_constructor.py::test_buns_tab[chrome] PASSED [ 26%]
tests/test_constructor.py::test_buns_tab[firefox] PASSED [ 30%]
tests/test_constructor.py::test_sauces_tab[chrome] PASSED [ 34%]
tests/test_constructor.py::test_sauces_tab[firefox] PASSED [ 38%]
tests/test_constructor.py::test_fillings_tab[chrome] PASSED [ 42%]
tests/test_constructor.py::test_fillings_tab[firefox] PASSED [ 46%]
tests/test_login.py::test_login_from_main_page[chrome] PASSED [ 50%]
tests/test_login.py::test_login_from_main_page[firefox] PASSED [ 53%]
tests/test_login.py::test_login_from_personal_account[chrome] PASSED [ 57%]
tests/test_login.py::test_login_from_personal_account[firefox] PASSED [ 61%]
tests/test_login.py::test_login_from_registration[chrome] PASSED [ 65%]
tests/test_login.py::test_login_from_registration[firefox] PASSED [ 69%]
tests/test_login.py::test_login_from_password_recovery[chrome] PASSED [ 73%]
tests/test_login.py::test_login_from_password_recovery[firefox] PASSED [ 76%]
tests/test_logout.py::test_logout[chrome] PASSED [ 80%]
tests/test_logout.py::test_logout[firefox] PASSED [ 84%]
tests/test_registration.py::test_successful_registration[chrome] PASSED [ 88%]
tests/test_registration.py::test_successful_registration[firefox] PASSED [ 92%]
tests/test_registration.py::test_registration_with_invalid_password[chrome] PASSED [ 96%]
tests/test_registration.py::test_registration_with_invalid_password[firefox] PASSED  