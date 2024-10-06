#features/steps/home_steps.py

from behave import given, when, then
from selenium import webdriver
from pages.home_page import HomePage
from pages.alerts_frames_windows_page import AlertsFramesWindowsPage
import os
import logging

# No início do seu arquivo de step definitions
screenshots_path = os.path.join(os.getcwd(), 'screenshots')
reports_path = os.path.join(os.getcwd(), 'reports')

os.makedirs(screenshots_path, exist_ok=True)
os.makedirs(reports_path, exist_ok=True)


# Configuração básica de logging
logging.basicConfig(level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s', 
                    filename='selenium_behave.log')

# Cenário 2

@when('I navigate to "Widgets"')
def step_navigate_to_widgets(context):
    logging.info("Navegando para 'Widgets'")
    context.alerts_page.click_browser_windows()
    # Captura a screenshot
    screenshots_path = os.path.join(os.getcwd(), 'screenshots',
                                    'widgets_windows.png')
    context.driver.save_screenshot(screenshots_path)
    logging.info("'Widgets' clicado e screenshot capturada.")
    
    
@when('I click on "Widgets" button')
def step_click_widgets_button(context):
    logging.info("Clicando no botão 'Widgets'")
    context.alerts_page.click_widgets_window()
    # Captura a screenshot
    screenshots_path = os.path.join(os.getcwd(), 'screenshots', 
                                    'widgets_clicked.png')
    context.driver.save_screenshot(screenshots_path)
    logging.info("'Widgets' clicado e screenshot capturada.")

@when('I navigate to "Progress Bar"')
def step_navigate_to_progress_bar(context):
    logging.info("Navegando para 'Progress Bar'")
    context.alerts_page.click_progress_bar()
    # Captura a screenshot
    screenshots_path = os.path.join(os.getcwd(), 'screenshots', 'progress_windows.png')
    context.driver.save_screenshot(screenshots_path)
    logging.info("'progress bar' clicado e screenshot capturada.")

@when('I validate the progress bar at 25%')
def validate_progress_bar(context):
    logging.info("Validando a porcentagem")
    context.alerts_page.validate_progress_bar()
    # Captura screenshot
    screenshots_path = os.path.join(os.getcwd(), 'screenshots', 'carregamento.png')
    context.driver.save_screenshot(screenshots_path)
    logging.info("'progress bar' clicado e screenshot capturada.")
    

