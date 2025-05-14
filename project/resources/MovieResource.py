import requests

class MovieResource:
    BASE_URL = "https://api.kinopoisk.dev/v1.4/movie"

    def __init__(self, token):
        self.token = token
        self.headers = {'X-API-KEY': token}

    def fetch_movies(self, params):
        print("📌 REQUEST PARAMETERS:", params)  # 🔥 Выводим параметры перед отправкой
        response = requests.get(self.BASE_URL, params=params, headers=self.headers)
        return response.json()