valid_email = ""
valid_pass = ""

invalid_email = 'xcbhgzgmail.com'
invalid_pass = 'fgsvvw15'

name = 'Иван'
surname = 'Иванов'
region = 'Москва г'
email = 'cvfhtjy@gmail.com'
password = '1Xdsf235'

false_email = 'cvfhtjy@gmail,ru'
false_mobile_max = '890913945236'
false_mobile_mini = '8909139452'
false_name_mini = 'Й'
name_two_letters = "Аб"
thirty_letters = 'Данныйпараметрпоказываетколиче'
thirtyone_letters = 'Данныйпараметрпоказываетколичес'

class TestData:
    BASE_URL = 'https://b2c.passport.rt.ru/'

    #Заголовки названий элементов
    FORM_AUTH_MAIL = 'Почта'
    AUTH = 'Авторизация'
    RECOVERY = 'Восстановление пароля'
    CHECK = 'Регистрация'
    VERIFICATION_EMAIL = 'Подтверждение email'
    VERIFICATION_INVALID_EMAIL = 'Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru'
    VERIFICATION_INVALID_NAME = 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'