import os
from typing import Dict

class PersonFinderView():
    def person_finder_view(self) -> Dict:

        os.system("cls||clear")

        print(f"{'='*100}")
        print(f"{'Encontrar Pessoa':^100}\n\n")
        print(f"{'='*100}")
        
        name = input("Informe o primeiro nome: ").capitalize().strip()
        lastname = input("Informe o úlimo sobrenome: ").capitalize().strip()

        person_finder_informations ={
            "name": name,
            "lastname": lastname
        }

        return person_finder_informations
    
    def person_finder_sucess(self, message: Dict) -> None:
        os.system("cls||clear")

        success_message = f'''Usuário encontrado com sucesso!

            Tipo: { message["message"]["type"] },
            Registros: { message["message"]["count"] },
            Infos: { message["message"]["person_informations"]["name"]} '''
        
        print(message)

    
    def person_finder_fail(self, error: str) -> None:
        os.system("cls||clear")

        fail_message = f'''Usuário não encontrado!
            Erro: { error }
        '''
        
        print(fail_message)
