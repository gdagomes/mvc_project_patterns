from src.view.person_register_view import PersonRegisterView
from src.controller.person_register_controller import PersonRegisterController

def person_register_constructor():
    
    # Instanciando a página de registro
    new_person = PersonRegisterView()
    
    # acionando o método de registro
    new_person_informations = new_person.person_register_view()

    # encaminha o registro para que o controler realiza a lógica
    new_register = PersonRegisterController()

    complete_request = new_register.person_register(new_person_informations)

    # encaminha o resultado para que a view informe ao cliente
    if complete_request["success"]:
        
        new_person.person_register_success_view(complete_request)

    else:
        pass