# language: pt
Funcionalidade: Criar, Editar e Deletar um novo registro
    '''
    Eu como usuário quero acessar a pagina elements na no menu inicial
    e acessar o menu webtables
    e criar, alterar e deletar um novo registro

    '''
    Cenário: Criar um novo registro
        Dado que eu acesse a pagina inicial de "https://demoqa.com"
        Quando eu cliclo no menu "Elements"
        E eu clico no submenu "Web Tables"
        E clico no botão "Add"
        E preencho a informação "First Name"
        E preencho a informação "Last Name"
        E preencho a informação "Age"
        E preencho a informação "Email"
        E preencho a informação "Salary"
        E preencho a informação  "Department"
        E clico no botão "Submit"
        Então o cadastro deve ser realizado com sucesso

