import pytest
import allure
from services.MoviesService import MoviesService
from services.PersonService import PersonService
from services.SearchService import SearchService

@pytest.fixture(scope="session")
def movie_service():
    token = "CRC3A21-NBJ4CMN-NKNDX3F-G271NN9"
    return MoviesService(token)

@pytest.fixture(scope="session")
def person_service():
    token = "CRC3A21-NBJ4CMN-NKNDX3F-G271NN9"
    return PersonService(token)

@pytest.fixture(scope="session")
def search_service():
    token = "CRC3A21-NBJ4CMN-NKNDX3F-G271NN9"
    return SearchService(token)

# Тест №1: Получение криминальных фильмов
@allure.feature('API Tests')  # Группа тестов
@allure.story('Получение фильмов по жанру')  # История теста
@allure.severity(allure.severity_level.NORMAL)  # Уровень важности
def test_fetch_criminal_movies(movie_service):
    with allure.step("Получаем криминальные фильмы"):  # Комментарии шага
        result = movie_service.get_movies_by_params(year=2024, genre='криминал', limit=10)
        assert len(result['docs']) > 0, "Фильмов не найдено!"

# Тест №2: Поиск мультфильмов
@allure.feature('API Tests')
@allure.story('Получение мультфильмов')
@allure.severity(allure.severity_level.MINOR)
def test_fetch_cartoons(movie_service):
    with allure.step("Получаем мультфильмы"):
        result = movie_service.get_movies_by_params(type='cartoon', limit=5)
        assert len(result['docs']) > 0, "Мультфильмов не найдено!"

# Тест №3: Поиск персоны
@allure.feature('API Tests')
@allure.story('Поиск персоны')
@allure.severity(allure.severity_level.NORMAL)
def test_person_search(person_service):
    with allure.step("Ищем персону Brad Pitt"):
        result = person_service.search_person(query="Brad Pitt")
        assert len(result['docs']) > 0, "Ни одной персоны не найдено!"

# Тест №4: Поиск фильмов по имени актера
@allure.feature('API Tests')
@allure.story('Поиск фильмов по персонажу')
@allure.severity(allure.severity_level.CRITICAL)
def test_search_films(search_service):
    with allure.step("Ищем фильмы с участием Брэда Питта"):
        result = search_service.search_film(query="Brad Pitt")
        assert len(result['docs']) > 0, "Фильмов не найдено!"

# Тест №5: Поиск фильмов по названию
@allure.feature('API Tests')
@allure.story('Поиск фильмов по названию')
@allure.severity(allure.severity_level.BLOCKER)
def test_search_by_title(search_service):
    with allure.step("Ищем фильм Матрица Революция"):
        result = search_service.search_film(query="Матрица революция")
        assert len(result['docs']) > 0, "Фильмов не найдено!"