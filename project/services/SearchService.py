from resources.SearchResource import SearchResource

class SearchService:
    def __init__(self, token):
        self.search_resource = SearchResource(token)

    def search_film(self, query):
        return self.search_resource.search_film(query)