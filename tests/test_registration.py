from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators import Locators
import random
import time


class TestRegistrationPage:
    def test_successful_registration(self, driver):
        # Переход на страницу регистрации
        driver.find_element(*Locators.LOGIN_BUTTON_MAIN).click()
        time.sleep(2)

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(Locators.REGISTER_LINK)
        ).click()

        # Проверяем, что перешли на страницу регистрации
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.REGISTER_SUBMIT_BUTTON)
        )
        assert "Регистрация" in driver.page_source

    def test_registration_with_short_password(self, driver):
        # Переход на страницу регистрации
        driver.find_element(*Locators.LOGIN_BUTTON_MAIN).click()
        time.sleep(2)

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(Locators.REGISTER_LINK)
        ).click()

        # Форма с коротким паролем
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.NAME_INPUT_REGISTER)
        )

        name = "Test User"
        email = f"test{random.randint(1000, 9999)}@example.com"
        password = "12345"

        driver.find_element(*Locators.NAME_INPUT_REGISTER).send_keys(name)
        driver.find_element(*Locators.EMAIL_INPUT_REGISTER).send_keys(email)
        driver.find_element(*Locators.PASSWORD_INPUT_REGISTER).send_keys(password)
        driver.find_element(*Locators.REGISTER_SUBMIT_BUTTON).click()

        # Проверяем сообщение об ошибке
        time.sleep(2)
        assert "Некорректный пароль" in driver.page_source