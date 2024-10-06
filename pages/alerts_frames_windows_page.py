# pages/alerts_frames_windows_page.py

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AlertsFramesWindowsPage:
    def __init__(self, driver):
        self.driver = driver
        self.browser_windows_xpath = "//span[text()='Browser Windows']"
        self.new_window_button_xpath = "//button[text()='New Window']"
        self.message_xpath = "//h1[text()='This is a sample page']"
        self.widgets_xpath = "/html/body/div[2]/div/div/div[2]/div/div[4]/div/div[3]"
        self.widgets_button_xpath = "/html/body/div[2]/div/div/div[2]/div/div[4]/div/div[3]"
        self.progrees_bar = "//span[text()='Progress Bar']"

    def click_browser_windows(self):
        element = self.driver.find_element(By.XPATH, self.browser_windows_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()

    def click_new_window(self):
        element = self.driver.find_element(By.XPATH, self.new_window_button_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()

    def switch_to_new_window(self):
        WebDriverWait(self.driver, 10).until(EC.number_of_windows_to_be(2))
        new_window = self.driver.window_handles[1]
        self.driver.switch_to.window(new_window)

    def validate_new_window_message(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.message_xpath))
        )
        element = self.driver.find_element(By.XPATH, self.message_xpath)
        return element.is_displayed()
    
    def click_widgets_window(self):
        element = self.driver.find_element(By.XPATH, self.widgets_button_xpath)
        WebDriverWait(self.driver, 10).until(EC.number_of_windows_to_be(1))
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()
        
    def click_progress_bar(self):
        element = self.driver.find_element(By.XPATH, self.progrees_bar)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()
    
    def validate_progress_bar(self):
        # Localiza e clica no botão de iniciar/parar a barra de progresso
        start_button = self.driver.find_element(By.ID, 'startStopButton')
        self.driver.execute_script("arguments[0].scrollIntoView();", start_button)
        
        # Iniciar a barra de progresso
        start_button.click()
        
        # Esperar até que a barra de progresso atinja 25%
        WebDriverWait(self.driver, 20).until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#progressBar .progress-bar'), '25%')
        )

        # Verificar o valor atual da barra de progresso
        progress_value = self.driver.find_element(By.CSS_SELECTOR, "#progressBar .progress-bar").get_attribute("aria-valuenow")
        assert progress_value == "25", f"Expected progress to be 25%, but got {progress_value}%"
        
        # Clicar novamente no botão para continuar até 100%
        start_button.click()

        # Esperar até que a barra de progresso atinja 100%
        WebDriverWait(self.driver, 20).until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#progressBar .progress-bar'), '100%')
        )
            