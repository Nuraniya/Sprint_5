from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from locators import Locators


class TestProfilePage:
    def test_navigate_to_personal_account(self, driver):
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.LOGIN_SUBMIT_BUTTON)
        )
        assert "Вход" in driver.page_source

    def test_navigate_from_personal_account_to_constructor_via_button(self, driver):
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.LOGIN_SUBMIT_BUTTON)
        )

        driver.find_element(*Locators.CONSTRUCTOR_BUTTON).click()

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//h1[contains(text(), 'Соберите бургер')]"))
        )
        assert "Соберите бургер" in driver.page_source

    def test_navigate_from_personal_account_to_constructor_via_logo(self, driver):
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.LOGIN_SUBMIT_BUTTON)
        )

        driver.find_element(*Locators.LOGO).click()

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//h1[contains(text(), 'Соберите бургер')]"))
        )
        assert "Соберите бургер" in driver.page_source

    def test_logout_from_personal_account(self, driver):
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.LOGIN_SUBMIT_BUTTON)
        )
        assert "Вход" in driver.page_source