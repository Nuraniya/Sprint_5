import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    # версия без webdriver_manager
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")
    driver.maximize_window()
    yield driver
    driver.quit()