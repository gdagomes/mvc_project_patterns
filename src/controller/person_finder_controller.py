from typing import Dict
from src.models.repository.person_repository import person_repository
from src.models.entities.person import Person

class PersonFinderController:
    def find_by_name(self, person_finder_informations: Dict) -> Dict:
        try:
            self.__validate_fields(person_finder_informations)
            pessoa = self.__find_person(person_finder_informations)

            return { "success": True, "message":  self.__format_response(pessoa, "200 OK") }
        
        except Exception as error:

            return { "success": False, "error": str(error), "message":  self.__format_response(person_finder_informations, "400 Bad Request") }

    
    def __validate_fields (self, person_finder_informations: Dict ) -> None:
        name = person_finder_informations['name']
        last_name = person_finder_informations['lastname']
        
        valid_data = name.isdigit() or last_name.isdigit() 

        if valid_data:
            raise Exception('Campo Nome/Sobrenome inválido!')
        

    def __find_person(self,person_finder_informations: Dict ) -> Person:
        name = person_finder_informations["name"]
        lastname = person_finder_informations["lastname"]

        person = person_repository.find_person_by_name(name, lastname)

        if not person:
            raise Exception("Pessoa não encontrada!")
        
        return person


    def __format_response(self, person: Person, status_code: str) -> Dict:
        
        if person: 
            return {
                    "count": id,
                    "type": "Person", 
                    "person_informations": {
                        "name": {person.name}, 
                        "lastname":{person.lastname},
                        "age":{person.age}
                    }
                }
        return None