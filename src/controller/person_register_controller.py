from typing import Dict
from src.models.repository.person_repository import person_repository
from src.models.entities.person import Person

class PersonRegisterController:

    def person_register(self, new_person_informations: Dict ) -> Dict:
        try: 
            self.__validate_fields(new_person_informations)
            self.__register_new_person(new_person_informations)

            return {"success": True, "message":  self.__format_response(new_person_informations, "201 Created") }
        
        except Exception as error:
            return {"success": False, "error": str(error), "message":  self.__format_response(new_person_informations, "400 Bad Request") }

    
    def __validate_fields(self, new_person_informations: Dict) -> None:
            name= new_person_informations['name']
            last_name = new_person_informations['lastname']
           
            valid_data = name.isdigit() or last_name.isdigit() 

            if valid_data:
                raise Exception('Campo Nome/Sobrenome inválido!')
            
            try:
                int(new_person_informations['age'])
            except:
                raise Exception('Campo Idade não é um número inteiro.')
        

    def __register_new_person(self, new_person_informations: Person) -> None:
        
        name = new_person_informations["name"]
        lastname = new_person_informations["lastname"]
        age = new_person_informations["age"]

        new_person = Person(name, lastname, age )
        person_repository.registry_person(new_person)


    def __format_response(self, new_person_informations: Dict, status_code: str) -> Dict:
        return { "Status Code": status_code, "new_person_informations": new_person_informations }