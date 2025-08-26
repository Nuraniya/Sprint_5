import random

#
class TestData:
    @staticmethod
    def generate_name():
        return "Nuraniya Suleymanova"

    @staticmethod
    def generate_email():
        return f"nuraniya_suleymanova_29_{random.randint(100, 999)}@yandex.ru"

    @staticmethod
    def generate_password():
        return f"Qwe{random.randint(100, 999)}"

    @staticmethod
    def generate_short_password():
        return "12345"
