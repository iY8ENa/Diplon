from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class FilmPage:
    def __init__(self, driver):
        self.driver = driver

    # Локаторы элементов на странице фильма
    DESCRIPTION_LOCATOR = (By.CSS_SELECTOR, "p.styles_paragraph__wEGPz")  # Описание фильма
    ACTORS_LOCATOR = (By.CSS_SELECTOR, "div.styles_actors__wn_C4")  # Актёры
    TRAILERS_LOCATOR = (By.CSS_SELECTOR, "video,iframe")  # Трейлер (видеоэлементы или iframe)
    RATING_LOCATOR = (By.CSS_SELECTOR, "span.styles_ratingKpTop__84afd")  # Оценка
    RETURN_HOME_BUTTON_LOCATOR = (By.CSS_SELECTOR, "#__next > div.styles_root__vsmL9 > div.styles_root__BJH2_.styles_headerContainer__sFBK8 > header > div > div.styles_logoContainer__G47EP > div > a > img")

    def verify_description_is_visible(self):
        """Проверяет наличие описания фильма."""
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.DESCRIPTION_LOCATOR))
            return True
        except Exception:
            return False

    def verify_actors_are_visible(self):
        """Проверяет наличие раздела с актёрами."""
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.ACTORS_LOCATOR))
            return True
        except Exception:
            return False

    def verify_trailers_are_visible(self):
        """Проверяет наличие трейлера."""
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_any_elements_located(self.TRAILERS_LOCATOR))
            return True
        except Exception:
            return False

    def verify_rating_is_visible(self):
        """Проверяет наличие рейтинга фильма."""
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.RATING_LOCATOR))
            return True
        except Exception:
            return False

    def navigate_back_to_homepage(self):
        """Возврат на главную страницу."""
        back_button = self.driver.find_element(*self.RETURN_HOME_BUTTON_LOCATOR)
        back_button.click()