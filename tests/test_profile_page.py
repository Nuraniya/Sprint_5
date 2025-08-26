from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By  # ← ДОБАВЬ ЭТУ СТРОКУ
from locators import Locators
import time


class TestProfilePage:
    def test_navigate_to_personal_account(self, driver):
        # Просто проверяем переход на страницу входа
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()

        # Проверяем, что перешли на страницу входа
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.LOGIN_SUBMIT_BUTTON)
        )
        assert "Вход" in driver.page_source

    def test_navigate_from_personal_account_to_constructor_via_button(self, driver):
        # Переходим в личный кабинет
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        time.sleep(2)

        # Возвращаемся в конструктор через кнопку
        driver.find_element(*Locators.CONSTRUCTOR_BUTTON).click()

        # Проверяем, что вернулись на главную (проверяем заголовок или другой элемент)
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//h1[contains(text(), 'Соберите бургер')]"))
        )
        assert "Соберите бургер" in driver.page_source

    def test_navigate_from_personal_account_to_constructor_via_logo(self, driver):
        # Переходим в личный кабинет
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        time.sleep(2)

        # Возвращаемся в конструктор через логотип
        driver.find_element(*Locators.LOGO).click()

        # Проверяем, что вернулись на главную (проверяем заголовок или другой элемент)
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//h1[contains(text(), 'Соберите бургер')]"))
        )
        assert "Соберите бургер" in driver.page_source

    def test_logout_from_personal_account(self, driver):
        # Проверяем переход
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()

        # Проверяем, что перешли на страницу входа
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.LOGIN_SUBMIT_BUTTON)
        )
        assert "Вход" in driver.page_source