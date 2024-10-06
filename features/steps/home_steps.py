# features/steps/home_steps.py

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
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', filename='selenium_behave.log')

@given('I am on the home page of "{url}"')
def step_open_home_page(context, url):
    logging.info(f"Abrindo a página inicial: {url}")
    context.driver = webdriver.Firefox()
    context.driver.implicitly_wait(10)
    context.driver.maximize_window()
    context.home_page = HomePage(context.driver)
    context.alerts_page = AlertsFramesWindowsPage(context.driver)
    context.home_page.open_home_page()
    # Captura a screenshot
    screenshots_path = os.path.join(os.getcwd(), 'screenshots', 'home_page.png')
    context.driver.save_screenshot(screenshots_path)
    logging.info("Página inicial aberta e screenshot capturada.")

@when('I click on "Alerts, Frame & Windows"')
def step_click_alerts_frame_windows(context):
    logging.info("Clicando em 'Alerts, Frame & Windows'")
    context.home_page.click_alerts_frames_windows()
    # Captura a screenshot
    screenshots_path = os.path.join(os.getcwd(), 'screenshots', 'alerts_frames_windows.png')
    context.driver.save_screenshot(screenshots_path)
    logging.info("'Alerts, Frame & Windows' clicado e screenshot capturada.")

@when('I navigate to "Browser Windows"')
def step_navigate_to_browser_windows(context):
    logging.info("Navegando para 'Browser Windows'")
    context.alerts_page.click_browser_windows()
    # Captura a screenshot
    screenshots_path = os.path.join(os.getcwd(), 'screenshots', 'browser_windows.png')
    context.driver.save_screenshot(screenshots_path)
    logging.info("'Browser Windows' clicado e screenshot capturada.")

@when('I click on "New Window" button')
def step_click_new_window_button(context):
    logging.info("Clicando no botão 'New Window'")
    context.alerts_page.click_new_window()
    # Captura a screenshot
    screenshots_path = os.path.join(os.getcwd(), 'screenshots', 'new_window_clicked.png')
    context.driver.save_screenshot(screenshots_path)
    logging.info("'New Window' clicado e screenshot capturada.")

@then('I should see a new window with the message "{message}"')
def step_validate_new_window_message(context, message):
    logging.info(f"Validando a mensagem na nova janela: '{message}'")
    context.alerts_page.switch_to_new_window()
    assert context.alerts_page.validate_new_window_message(),f"A mensagem '{message}'não foi encontrada na nova janela"
    # Captura a screenshot da nova janela
    screenshots_path = os.path.join(os.getcwd(), 'screenshots', 'new_window_message.png')
    context.driver.save_screenshot(screenshots_path)
    logging.info("Mensagem validada e screenshot capturada.")
    context.driver.quit()
    logging.info("Driver fechado.")

