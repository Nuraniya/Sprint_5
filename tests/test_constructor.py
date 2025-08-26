from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators import Locators


class TestConstructor:
    def test_navigate_to_buns_section(self, driver):
        # Переход к соусам, потом к булкам
        driver.find_element(*Locators.SAUCES_SECTION).click()
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.ACTIVE_SECTION)
        )

        # Переход к булкам
        driver.find_element(*Locators.BUNS_SECTION).click()

        # Проверка активации раздела
        WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element(Locators.ACTIVE_SECTION, "Булки")
        )
        active_section = driver.find_element(*Locators.ACTIVE_SECTION)
        assert "Булки" in active_section.text

    def test_navigate_to_sauces_section(self, driver):
        # Переход к соусам
        driver.find_element(*Locators.SAUCES_SECTION).click()

        # Проверка активации раздела
        WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element(Locators.ACTIVE_SECTION, "Соусы")
        )
        active_section = driver.find_element(*Locators.ACTIVE_SECTION)
        assert "Соусы" in active_section.text

    def test_navigate_to_fillings_section(self, driver):
        # Переход к начинкам
        driver.find_element(*Locators.FILLINGS_SECTION).click()

        # Проверка активации раздела
        WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element(Locators.ACTIVE_SECTION, "Начинки")
        )
        active_section = driver.find_element(*Locators.ACTIVE_SECTION)
        assert "Начинки" in active_section.text