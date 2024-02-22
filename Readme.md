# Projeto MVC

## Introdução

Este projeto foi desenvolvido para acompanhamento das video-aulas sobre arquitetura MVC (Model - View - Controller) do canal [Programador Lhama](https://www.youtube.com/watch?v=abqeIMr1hsg&list=PLAgbpJQADBGKvsjOu4gHU5E9WUQs8XRgS).



## O que é MVC?
MVC é um padrão de arquitetura de software que deu-se inicio em 1970 e vem evoluindo com o tempo.

Seu padrão consiste em dividir uma aplicação em três camadas, são elas:

* Model: 
  * Camada para manipulação dos Dados

* View:
  * Camada para interação com o usuário

* Controller:
  * Camada que realiza o Controle das trocas realizadas entre as camadas Model e View.

## Sobre o projeto
O projeto conta com a seguinte arquitetura:

- Projeto_MVC
  - src
    - controller
      - person_finder_controller.py
      - person_register_controller.py
    - models
      - entities
        - person.py
      - repository
        - person_repository.py
    - view
      - person_finder_view.py
      - person_register_view.py
      - person_registration_system_view.py
    - main
      - proccess_handle.py
      - constructor
        - person_finder_constructor.py
        - person_register_constructor.py
        - person_registration_system_constructor.py
  - run_app.py

### Observações

O script **procces_handle** incluso no diretório _main_, terá como responsabilidade transitar de forma harmônica entre as 3 camadas do MVC. 

Visualmente, o processo seria da seguinte maneira:

    View <-> Main <-> Controler <-> Main <-> Model