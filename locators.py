from selenium.webdriver.common.by import By


class Locators:
    # Главная страница
    LOGIN_BUTTON_MAIN = (By.XPATH, "//button[contains(text(), 'Войти в аккаунт')]")
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//p[contains(text(), 'Личный Кабинет')]")
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[contains(text(), 'Конструктор')]")
    LOGO = (By.XPATH, "//div[contains(@class, 'AppHeader_header__logo')]")
    ORDER_BUTTON = (By.XPATH, "//button[contains(text(), 'Оформить заказ')]")

    # Регистрация
    REGISTER_LINK = (By.XPATH, "//a[contains(text(), 'Зарегистрироваться')]")
    NAME_INPUT_REGISTER = (By.XPATH, "//label[contains(text(), 'Имя')]/following-sibling::input")
    EMAIL_INPUT_REGISTER = (By.XPATH, "//label[contains(text(), 'Email')]/following-sibling::input")
    PASSWORD_INPUT_REGISTER = (By.XPATH, "//input[@type='password']")
    REGISTER_SUBMIT_BUTTON = (By.XPATH, "//button[contains(text(), 'Зарегистрироваться')]")
    PASSWORD_ERROR = (By.XPATH, "//p[contains(@class, 'input__error')]")
    LOGIN_LINK_REGISTER = (By.XPATH, "//a[contains(text(), 'Войти')]")

    # Страница входа
    EMAIL_INPUT_LOGIN = (By.XPATH, "//input[@name='name']")
    PASSWORD_INPUT_LOGIN = (By.XPATH, "//input[@type='password']")
    LOGIN_SUBMIT_BUTTON = (By.XPATH, "//button[contains(text(), 'Войти')]")
    FORGOT_PASSWORD_LINK = (By.XPATH, "//a[contains(text(), 'Восстановить пароль')]")

    # Страница восстановления пароля
    LOGIN_LINK_RECOVERY = (By.XPATH, "//a[contains(text(), 'Войти')]")

    # Личный кабинет
    PROFILE_LINK = (By.XPATH, "//a[contains(text(), 'Профиль')]")
    LOGOUT_BUTTON = (By.XPATH, "//button[contains(text(), 'Выход')]")

    # Конструктор
    BUNS_SECTION = (By.XPATH, "//span[contains(text(), 'Булки')]/..")
    SAUCES_SECTION = (By.XPATH, "//span[contains(text(), 'Соусы')]/..")
    FILLINGS_SECTION = (By.XPATH, "//span[contains(text(), 'Начинки')]/..")
    ACTIVE_SECTION = (By.XPATH, "//div[contains(@class, 'tab_tab_type_current')]")