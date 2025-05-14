from resources.MovieResource import MovieResource

class MoviesService:
    def __init__(self, token):
        self.movie_resource = MovieResource(token)

    def get_movies_by_params(self, year=None, genre=None, type=None, limit=None):
        # Готовим параметры запроса
        params = {}
        if year:
            params['year'] = year
        if genre:
            params['genres.name'] = genre
        if type:
            params['type'] = type.lower()  # 🔥 Обеспечим нижний регистр для type
        if limit:
            params['limit'] = limit

        return self.movie_resource.fetch_movies(params)