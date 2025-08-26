import pytest
from selenium import webdriver
import random


@pytest.fixture
def driver():
    # версия без webdriver_manager
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")
    driver.maximize_window()
    yield driver
    driver.quit()


def generate_email():
    return f"ivan_ivanov_14_{random.randint(100, 999)}@yandex.ru"


def generate_password():
    return f"Qwe{random.randint(100, 999)}"


def generate_name():
    return "Ivan Ivanov"