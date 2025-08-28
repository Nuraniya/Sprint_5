from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from locators import Locators


class TestConstructor:

    def test_constructor_sections_displayed(self, driver):
        """Простой тест: проверяем, что разделы конструктора отображаются"""

        # Проверяем, что кнопки разделов видны
        buns_btn = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.BUNS_SECTION)
        )
        sauces_btn = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.SAUCES_SECTION)
        )
        fillings_btn = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.FILLINGS_SECTION)
        )

        assert buns_btn.is_displayed(), "Кнопка 'Булки' не отображается"
        assert sauces_btn.is_displayed(), "Кнопка 'Соусы' не отображается"
        assert fillings_btn.is_displayed(), "Кнопка 'Начинки' не отображается"

        print("✓ Все кнопки разделов отображаются")

    def test_constructor_has_ingredients(self, driver):
        """Простой тест: проверяем, что на странице есть ингредиенты"""

        # Ждем загрузки ингредиентов
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//h2[text()='Булки']"))
        )

        # Ищем любые ингредиенты на странице
        ingredients = driver.find_elements(By.XPATH, "//li | //div[contains(@class, 'ingredient')]")

        assert len(ingredients) > 0, "На странице нет ингредиентов"
        print(f"✓ Найдено ингредиентов: {len(ingredients)}")