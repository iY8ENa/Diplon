from selenium.webdriver.common.by import By


class PremieresPage:
    def __init__(self, driver):
        self.driver = driver

    # Локатор для заголовка страницы графики кинопремьер
    PREMIERES_HEADER_LOCATOR = (By.CSS_SELECTOR, "#seansPremHeader > h1")

    def verify_premieres_page_opened(self):
        """Проверяет, что открыта страница графика кинопремьер."""
        premieres_header = self.driver.find_element(*self.PREMIERES_HEADER_LOCATOR)
        return "График кинопремьер" in premieres_header.text