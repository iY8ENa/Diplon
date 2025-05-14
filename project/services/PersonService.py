from resources.PersonResource import PersonResource

class PersonService:
    def __init__(self, token):
        self.person_resource = PersonResource(token)

    def search_person(self, query):
        return self.person_resource.search_person(query)