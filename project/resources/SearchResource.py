import requests

class SearchResource:
    BASE_URL = "https://api.kinopoisk.dev/v1.4/movie/search"

    def __init__(self, token):
        self.token = token
        self.headers = {'X-API-KEY': token}

    def search_film(self, query):
        params = {'query': query}
        response = requests.get(self.BASE_URL, params=params, headers=self.headers)
        return response.json()