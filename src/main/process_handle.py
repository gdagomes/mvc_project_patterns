"""Process Handle aponta para os construtores"""

# importa a página inicial 
from .constructor.person_registration_system_constructor import introduction_process 

# importa a página de registro
from .constructor.person_register_constructor import person_register_constructor

# importa a página de Pesquisa
from .constructor.person_finder_constructor import person_finder_constructor

def start() -> None:
    while True:
        command = introduction_process() 

        if command == '1':
            person_register_constructor()
        elif command == '2':
            person_finder_constructor()
        elif command == '3':
            exit()
       