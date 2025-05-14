import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from tests.pages.HomePage import HomePage
from tests.pages.SearchPage import SearchPage
from tests.pages.FilmPage import FilmPage
from tests.pages.PremieresPage import PremieresPage
from selenium.webdriver.common.by import By
import allure


@pytest.fixture(scope="module")
def browser(request):
    service = ChromeService(executable_path=r"C:\API UI\chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    driver.set_window_size(1920, 1080)  # задаём размер окна
    request.node.driver = driver  # привязываем драйвер к каждому тесту
    yield driver
    driver.quit()


# Обработчик фиксации изображений при сбоях
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        mode = "a" if os.path.exists("failures") else "w"
        try:
            if hasattr(item, "driver"):
                xfail = hasattr(rep, "wasxfail")
                if (rep.skipped and xfail) or (rep.failed and not xfail):
                    screenshot_data = item.driver.get_screenshot_as_png()
                    allure.attach(screenshot_data, name=f"Screenshot_{item.name}", attachment_type=allure.attachment_type.PNG)
        finally:
            pass


# Первый тест — проверка загрузки главной страницы
@allure.feature('Главная страница')
@allure.story('Проверка загрузки главной страницы')
def test_load_home_page(browser):
    home_page = HomePage(browser)
    home_page.go_to_homepage()
    home_page.wait_for_captcha_manual_input()

    with allure.step("Проверка загрузки главной страницы"):
        assert home_page.is_loaded(), "Главная страница не загружена правильно."
        expected_title = "Кинопоиск. Онлайн кинотеатр. Фильмы сериалы мультфильмы и энциклопедия"
        actual_title = home_page.title
        assert expected_title == actual_title, f"Ожидаемый заголовок '{expected_title}' не найден. Получено: {actual_title}"

    # Возвращаемся на главную страницу после окончания теста
    home_page.go_to_homepage()


# Второй тест — проверка поиска фильма
@allure.feature('Поиск фильма')
@allure.story('Проверка поиска фильма')
def test_search_movie(browser):
    home_page = HomePage(browser)
    home_page.go_to_homepage()
    home_page.wait_for_captcha_manual_input()

    with allure.step(f"Проводим поиск фильма \"Матрица\""):
        movie_name = "Матрица"
        home_page.search_movie(movie_name)

    with allure.step("Проверка наличия результатов поиска"):
        search_page = SearchPage(browser)
        assert search_page.has_result_with_text(movie_name), f"По запросу \"{movie_name}\" ничего не найдено!"

    # Возвращаемся на главную страницу после окончания теста
    home_page.go_to_homepage()


# Третий тест — проверка карточки фильма
@allure.feature('Карточка фильма')
@allure.story('Проверка страницы фильма')
def test_check_film_card(browser):
    home_page = HomePage(browser)
    home_page.go_to_homepage()
    home_page.wait_for_captcha_manual_input()

    with allure.step("Поиск фильма \"Интерстеллар\""):
        movie_name = "Интерстеллар"
        home_page.search_movie(movie_name)

    with allure.step("Выбор первого результата поиска"):
        home_page.select_first_search_result()

    with allure.step("Проверка основных блоков на странице фильма"):
        film_page = FilmPage(browser)
        assert film_page.verify_description_is_visible(), "Описание фильма не отображается."
        assert film_page.verify_actors_are_visible(), "Раздел с актёрами не отображается."
        assert film_page.verify_trailers_are_visible(), "Раздел с трейлерами не отображается."
        assert film_page.verify_rating_is_visible(), "Рейтинг фильма не отображается."

    # Возвращаемся на главную страницу после окончания теста
    film_page.navigate_back_to_homepage()


# Четвёртый тест — проверка открытия страницы топ-250 фильмов
@allure.feature('Топ-250 фильмов')
@allure.story('Проверка страницы топ-250 фильмов')
def test_open_top_250_movies(browser):
    home_page = HomePage(browser)
    home_page.go_to_homepage()
    home_page.wait_for_captcha_manual_input()

    with allure.step("Переход на страницу топ-250 фильмов"):
        home_page.open_top_250_movies()

    # Возвращаемся на главную страницу после окончания теста
    home_page.go_to_homepage()


# Пятый тест — проверка графика кинопремьер
@allure.feature('График кинопремьер')
@allure.story('Проверка графика кинопремьер')
def test_premieres_calendar(browser):
    home_page = HomePage(browser)
    home_page.go_to_homepage()
    home_page.wait_for_captcha_manual_input()

    with allure.step("Переход в категорию \"Фильмы\""):
        films_category_link = browser.find_element(By.CSS_SELECTOR, "#__next > div.styles_root__nRLZC > div.styles_middleContainer__K7dth.styles_baseContainer__AWlLR > div.styles_mainContainer__d7tsS > div > div > div.styles_column__r2MWX.styles_lg_5__tZpX0.styles_column__Wqs7y.styles_sidebarColumn__kpYI5 > div > div > div > nav > ul > li:nth-child(3) > a")
        films_category_link.click()

    with allure.step("Переход на страницу графика кинопремьер"):
        calendar_link = browser.find_element(By.CSS_SELECTOR, "#__next > div.styles_root__vsmL9 > div.styles_contentContainer__bi2n2.styles_baseContainer__8XBMw > div.styles_header__Mb2uW > ul > li:nth-child(2) > a")
        calendar_link.click()

    with allure.step("Проверка открытой страницы графика кинопремьер"):
        premieres_page = PremieresPage(browser)
        assert premieres_page.verify_premieres_page_opened(), "Страница графика кинопремьер не открылась."

    # Возвращаемся на главную страницу после окончания теста
    home_page.go_to_homepage()