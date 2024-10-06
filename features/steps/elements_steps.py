@given(u'que eu acesse a pagina inicial de "https://demoqa.com"')
def step_impl(context):
    context.home_page.open_home_page()


@when(u'eu cliclo no menu "Elements"')
def step_impl(context):
    context.home_page.menu_elements()
    context.element.wait_for_page_load()


@when(u'eu clico no submenu "Web Tables"')
def step_impl(context):
    context.element.web_table_click()


@when(u'clico no botão "Add"')
def step_impl(context):
    context.element.add_button_click()
    context.web_table.form()


@when(u'preencho a informação "First Name"')
def step_impl(context):
    context.web_table.first_name()


@when(u'preencho a informação "Last Name"')
def step_impl(context):
    context.web_table.last_name()


@when(u'preencho a informação "Age"')
def step_impl(context):
    context.web_table.data_nascimento()


@when(u'preencho a informação "Email"')
def step_impl(context):
    context.web_table.email()


@when(u'preencho a informação "Salary"')
def step_impl(context):
    context.web_table.salario_base()


@when(u'preencho a informação  "Department"')
def step_impl(context):
    context.web_table.departament()


@when(u'clico no botão "Submit"')
def step_impl(context):
   context.web_table.enviar_formulario()


@then(u'o cadastro deve ser realizado com sucesso')
def step_impl(context):
    context.web_table.get_cadastro()