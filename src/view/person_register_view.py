import os
from typing import Dict

class PersonRegisterView:
    
    def person_register_view(self)-> Dict:
       
        os.system("cls||clear")

        print(f"{'Registrar Nova Pessoa':^100}\n\n")

        name = input("Informe o primeiro nome: ").capitalize().strip()
        lastname = input("Informe o último sobrenome nome: ").capitalize().strip()
        age = input("Informe a idade atual: ")

        new_person_informations = {
            "name": name,
            "lastname": lastname,
            "age": age
        }

        return new_person_informations
    

    def person_register_success_view(self, response: Dict): 

        if response["success"]:
            os.system("cls||clear")

            print(f"{'='*100}")
            print(f"{'Cadastro Realizado com Sucesso':^100}")
            print(f"{'='*100}")
            
        else:
            print(f"{'='*100}")
            print(f"""{'Não foi possível realizar o cadastro':^100}\n\n {response}""")
            print(f"{'='*100}")

