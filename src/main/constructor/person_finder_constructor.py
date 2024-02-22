from src.view.person_finder_view import PersonFinderView
from src.controller.person_finder_controller import PersonFinderController


def person_finder_constructor():

    person_finder_view = PersonFinderView()
    person_finder_controller = PersonFinderController()

    person_finder_informations = person_finder_view.person_finder_view()
    response = person_finder_controller.find_by_name(person_finder_informations)

    if response["success"]:
        
        person_finder_view.person_finder_sucess(response)
    
    else:
       
        person_finder_view.person_finder_fail(response["error"])