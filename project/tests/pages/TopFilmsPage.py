from selenium.webdriver.common.by import By


class TopFilmsPage:
    def __init__(self, driver):
        self.driver = driver

    # Локатор для заголовка страницы топ-250 фильмов
    TOP_FILMS_TITLE_LOCATOR = (By.CSS_SELECTOR, "h1.styles_title__jB8AZ")  # Исправленный локатор

    def verify_top_films_page_opened(self):
        """Проверяет открытие страницы топ-250 фильмов."""
        top_films_title = self.driver.find_element(*self.TOP_FILMS_TITLE_LOCATOR)
        return "250 лучших фильмов" in top_films_title.text