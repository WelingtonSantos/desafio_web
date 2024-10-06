from selenium import webdriver
from behave import given, when, then
from pages.home_page import HomePage
from pages.elements import Element
from pages.web_tables import WebTables


def before_all(context):
    """Antes de todas as coisas acontecerem"""
    context.browser = webdriver.Chrome()
    context.home_page = HomePage(context.browser)
    context.element = Element(context.browser)
    context.web_table = WebTables(context.browser)
    
def after_step(context, step):
    """Execução depois de cada step"""
    pass

def after_all(context):
    """Execução após todo cenário for finalizado"""
    pass