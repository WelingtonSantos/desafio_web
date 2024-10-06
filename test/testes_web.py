from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

class ProgressBarPage:
    
    def __init__(self, driver):
        self.driver = driver

    def click_start_button(self):
        try:
            # Localizar o botão e clicar
            #start_button = self.driver.find_element(By.ID, "startStopButton")
            # Esperar até que o botão 'Start' esteja presente e visível
            start_button = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.ID, "startStopButton"))
            )
            # Scroll para o botão, se necessário
            self.driver.execute_script("arguments[0].scrollIntoView();", start_button)
            start_button.click()
            print("Botão 'Start' clicado.")
        except Exception as e:
            print(f"Erro ao clicar no botão: {e}")

    def wait_for_progress(self, expected_value):
        try:
            # Esperar que a barra de progresso esteja presente
            progress_bar = WebDriverWait(self.driver, 15).until(
                EC.presence_of_element_located((By.CLASS_NAME, "progress-bar"))
            )
            
            # Aguardar até que o valor 'aria-valuenow' atinja o valor esperado (ex: 25% ou 100%)
            WebDriverWait(self.driver, 10).until(
                lambda driver: progress_bar.get_attribute("aria-valuenow") == expected_value
            )
            
            print(f"Barra de progresso carregada a {expected_value}%.")
        #    self.driver.save_full_page_screenshot(f"ress_bar_timeout_{expected_value}.png")
            
        except TimeoutException:
            print(f"Erro: A barra de progresso não atingiu {expected_value}% no tempo limite.")
            # Opcional: Captura de screenshot para depuração
            self.driver.save_full_page_screenshot(f"progress_bar_timeout_{expected_value}.png")
        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")

    def take_screenshot(self, filename):
        # Tirar o screenshot da página
        try:
            self.driver.save_full_page_screenshot(filename)
            print(f"Screenshot tirada e salva como {filename}.")
        except Exception as e:
            print(f"Erro ao tirar screenshot: {e}")

    def click_pause_button(self):
        try:
            # Localizar o botão (o mesmo botão muda para "Pause" durante o carregamento)
            #pause_button = self.driver.find_element(By.ID, "startStopButton")
            pause_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.ID, "startStopButton"))
            )
            self.driver.execute_script("arguments[0].scrollIntoView();", pause_button)
            pause_button.click()
            print("Botão 'Pause' clicado.")
        except Exception as e:
            print(f"Erro ao pausar o carregamento: {e}")
    
#def remove_ads_via_js(driver):
#    try:
#        # Exemplo: remover elementos com a classe 'ad-class' (ajuste conforme necessário)
#        ads = driver.find_elements(By.CLASS_NAME, 'Google-Ad')
#        for ad in ads:
#            driver.execute_script("arguments[0].remove();", ad)
#            print("Anúncios removidos via JavaScript.")
#    except Exception as e:
#        print(f"Erro ao tentar remover anúncios via JavaScript: {e}")
def remove_ads_via_js(driver):
    try:
        # XPaths dos elementos de anúncios
        ad_selectors = [
            "//div[contains(@class, 'Google-Ad')]",
            "//div[contains(@id, 'banner')]",
            "//div[contains(@class, 'GoogleCreativeContainerClass')]"
        ]
                    # Tentar remover o iframe que pode estar causando o erro
        ads_iframes = driver.find_elements(By.XPATH, "//iframe[contains(@id, 'google_ads_iframe')]")
        for iframe in ads_iframes:
            driver.execute_script("arguments[0].remove();", iframe)
            print("Elemento iframe removido para permitir interação.")

        for selector in ad_selectors:
            # Localiza os anúncios usando o XPath
            ads = driver.find_elements(By.XPATH, selector)
            for ad in ads:
                driver.execute_script("arguments[0].remove();", ad)
                print(f"Anúncio removido via JavaScript: {selector}")

    except Exception as e:
        print(f"Erro ao tentar remover anúncios via JavaScript: {e}")


# Inicializar o driver do Selenium
driver = webdriver.Firefox()

# Navegar até a página da barra de progresso
driver.get("https://demoqa.com/progress-bar")

remove_ads_via_js(driver)
# Instanciar a classe ProgressBarPage
progress_page = ProgressBarPage(driver)


# Clicar no botão para iniciar o carregamento
progress_page.click_start_button()

# Esperar o carregamento da barra até 25%
progress_page.wait_for_progress("25")
# Pausar o carregamento em 25% e tirar um screenshot
progress_page.click_pause_button()
progress_page.take_screenshot("progress_bar_25.png")

# Continuar o carregamento até 100% (clicar no botão novamente)
progress_page.click_start_button()

# Esperar o carregamento da barra até 100%
progress_page.wait_for_progress("100")

# Tirar o screenshot após o carregamento completo
progress_page.take_screenshot("progress_bar_100.png")

# Fechar o navegador
driver.quit()
