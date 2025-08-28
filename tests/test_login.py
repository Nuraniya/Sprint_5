from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators import Locators


class TestLogin:
    def test_login_from_main_page_button(self, driver):
        driver.find_element(*Locators.LOGIN_BUTTON_MAIN).click()

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.LOGIN_SUBMIT_BUTTON)
        )
        assert "Вход" in driver.page_source

    def test_login_from_personal_account_button(self, driver):
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.LOGIN_SUBMIT_BUTTON)
        )
        assert "Вход" in driver.page_source

    def test_login_from_registration_page(self, driver):
        driver.find_element(*Locators.LOGIN_BUTTON_MAIN).click()

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(Locators.REGISTER_LINK)
        ).click()

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(Locators.LOGIN_LINK_REGISTER)
        ).click()

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.LOGIN_SUBMIT_BUTTON)
        )
        assert "Вход" in driver.page_source

    def test_login_from_password_recovery_page(self, driver):
        driver.find_element(*Locators.LOGIN_BUTTON_MAIN).click()

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(Locators.FORGOT_PASSWORD_LINK)
        ).click()

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(Locators.LOGIN_LINK_RECOVERY)
        ).click()

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.LOGIN_SUBMIT_BUTTON)
        )
        assert "Вход" in driver.page_source