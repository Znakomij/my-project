import unittest
from src.my_package.main import perform_eda


class TestEDA(unittest.TestCase):
    def test_eda(self):
        # Проверка, что функция выполняется без ошибок
        try:
            perform_eda()
        except Exception as e:
            self.fail(f"EDA failed with exception: {e}")


if __name__ == "__main__":
    unittest.main()
