from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    # Локаторы элементов
    SEARCH_INPUT_LOCATOR = (By.CSS_SELECTOR, "#__next > div.styles_root__nRLZC > div.styles_root__BJH2_.styles_headerContainer__f7XqC > header > div > div.styles_mainContainer__faOVn.styles_hasSidebar__rU_E2 > div.styles_searchFormContainer__GyAL5 > div > form > div > input")
    SEARCH_BUTTON_LOCATOR = (By.CSS_SELECTOR, "#__next > div.styles_root__nRLZC > div.styles_root__BJH2_.styles_headerContainer__f7XqC > header > div > div.styles_mainContainer__faOVn.styles_hasSidebar__rU_E2 > div.styles_searchFormContainerWide__3taA3.styles_searchFormContainer__GyAL5 > div > form > div > div > button > svg")
    FILM_CATEGORY_LOCATOR = (By.CSS_SELECTOR, "#__next > div.styles_root__nRLZC > div.styles_middleContainer__K7dth.styles_baseContainer__AWlLR > div.styles_mainContainer__d7tsS > div > div > div.styles_column__r2MWX.styles_lg_5__tZpX0.styles_column__Wqs7y.styles_sidebarColumn__kpYI5 > div > div > div > nav > ul > li:nth-child(3) > a")
    TOP_250_MOVIES_LOCATOR = (By.CSS_SELECTOR, "#__next > div.styles_root__vsmL9 > div.styles_contentContainer__bi2n2.styles_baseContainer__8XBMw > div.styles_root__LL1E2 > div.styles_content__2mO6X > div > a:nth-child(1)")

    def search_movie(self, movie_name):
        """Ищем фильм."""
        search_field = self.driver.find_element(*self.SEARCH_INPUT_LOCATOR)
        search_field.clear()
        search_field.send_keys(movie_name)
        self.driver.find_element(*self.SEARCH_BUTTON_LOCATOR).click()
        # Ждём появления результатов поиска
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "block_left_pad")))

    def select_first_search_result(self):
        """Выбираем первый результат поиска (фильм)."""
        link_to_film = self.driver.find_element(By.CSS_SELECTOR, "#block_left_pad > div > div:nth-child(3) > div > div.info > p > a")
        link_to_film.click()

    def open_top_250_movies(self):
        """Переход на страницу топ-250 фильмов."""
        category_link = self.driver.find_element(*self.FILM_CATEGORY_LOCATOR)
        category_link.click()

        # Переход на страницу топ-250 фильмов
        top_250_link = self.driver.find_element(*self.TOP_250_MOVIES_LOCATOR)
        top_250_link.click()

    def go_to_homepage(self):
        """Переход на главную страницу."""
        self.driver.get("https://www.kinopoisk.ru/")

    def wait_for_captcha_manual_input(self):
        """Дожидаемся ручного ввода капчи."""
        print("Подождите 30 секунд для ручного ввода капчи...")
        from time import sleep
        sleep(30)

    def is_loaded(self):
        """Проверяет, что главная страница загружена."""
        return self.driver.find_element(*self.SEARCH_INPUT_LOCATOR).is_displayed()

    @property
    def title(self):
        return self.driver.title