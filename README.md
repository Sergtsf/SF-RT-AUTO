Дипломный проект: реальный кейс компании «Ростелеком Информационные Технологии»

1. Тестирование требований: Была изучена документация от заказчика и выявлены расхождения  текста и фактических элементов сайта. В прикрепленном файле расхождения отмечены красным фоном, комментарий зеленым курсивом.

2. Для тестирование сайта разработан 21 тест-кейс, обеспечивающий высокий процент тестового покрытия критически важных функций сайта.

3. Написан 21 автотест: для удобства и локализации разделен на 4 файла:
  test_auth_buttons.py - Проверка функциональности кнопок авторизации;
  test_auth_form.py - Проверка функции авторизации на сайте;
  test_registration_form.py - Проверка функции регистрации на сайте;
  test_social_buttons.py - Проверка функциональности кнопок перехода к авторизации через      социальные сети, а также Помощь и Пользовательское соглашение.

4. Был найден и оформлен дефект.

5. Использованы техники тест дизайна:
   
   Техника эквивалентного разбиения и анализ граничных значений;
   Попарное тестирование;
   Тестирование состояний и переходов;
   Таблица решений.
   
Техники тест дизайна были выбраны с учетом того, что будут тестироваться множество полей ввода регистрации и авторизации различными способами, используя различные символы. Получение смс кода и писем о подтверждении аккаунта, которые имеют срок действия.

7. Окружение: Windows 10 / Chrome 121.0.6167.161 / PyCharm Community Edition 2023.2.4/ pytest-selenium 4.0.0 / selenium 4.9.0 / pytest 6.2.5

8. Активно использовался DevTools для написания автотестов и мониторинга времени загрузки страниц.

Сроки запуска (путь к веб драйверу указать свой):

python -m pytest -v --driver Chrome --driver-path D:/chromedriver.exe tests/test_auth_buttons.py

python -m pytest -v --driver Chrome --driver-path D:/chromedriver.exe tests/test_auth_form.py

python -m pytest -v --driver Chrome --driver-path D:/chromedriver.exe tests/test_registration_form.py

python -m pytest -v --driver Chrome --driver-path D:/chromedriver.exe tests/test_social_buttons.py

!!!ВАЖНО!!!
В config.py необходимо ввести свои валидные данные для авторизации на сайте.

valid_email = ""

valid_pass = ""

В config_for_test.py необходимо указать свой путь к веб драйверу.  
   
