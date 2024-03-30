from page.main_page import (MainPage)
from config import TestData, valid_pass, valid_email, invalid_pass, invalid_email

import time


# Авторизация, используя валидные почту и пароль
def test_auth_mail(driver):
    main_page = MainPage(driver)
    main_page.input_keys(MainPage.USERNAME, valid_email)
    main_page.input_keys(MainPage.PASS, valid_pass)
    main_page.find_click(MainPage.BUTTON_INPUT)
    logout = main_page.is_visible(MainPage.BUTTON_LOGOUT)
    time.sleep(2)
    assert logout == True


# Авторизация, используя валидную почту и невалидный пароль
def test_invalid_auth_mail(driver):
    main_page = MainPage(driver)
    main_page.input_keys(MainPage.USERNAME, valid_email)
    main_page.input_keys(MainPage.PASS, invalid_pass)
    main_page.find_click(MainPage.BUTTON_INPUT)
    error = main_page.is_visible(MainPage.ERROR_USERNAME_PASS)
    time.sleep(2)
    assert error == True


# Авторизация, используя невалидную почту и валидный пароль
def test_email_invalid_auth_mail(driver):
    main_page = MainPage(driver)
    main_page.input_keys(MainPage.USERNAME, invalid_email)
    main_page.input_keys(MainPage.PASS, valid_pass)
    main_page.find_click(MainPage.BUTTON_INPUT)
    error_username = main_page.is_visible(MainPage.ERROR_USERNAME_PASS)
    time.sleep(2)
    assert error_username == True
