from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import (
    NoSuchElementException,
    TimeoutException,
    ElementNotInteractableException
)
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Inicialização do WebDriver (Firefox neste exemplo)
driver = webdriver.Firefox()

# Abrir a página web
driver.get("https://demoqa.com/progress-bar")  # Substitua pela URL real

class PageWithAds:
    def __init__(self, driver):
        self.driver = driver

    # Mapeamento de elementos (ajuste conforme necessário)
    navbar_toggler = (By.CSS_SELECTOR, "button.navbar-toggler")
    ads_container = (By.CSS_SELECTOR, "div.col-12.mt-4.col-md-3")  # Ajuste conforme a estrutura real da página

    # Método para fechar ou ignorar o anúncio
    def ignore_ads(self):
        try:
            # Espera o contêiner de anúncios estar presente
            ads = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.ads_container)
            )
            if ads.is_displayed():
                try:
                    # Encontra o botão de fechar (navbar-toggler)
                    navbar = self.driver.find_element(*self.navbar_toggler)
                    # Rola até o botão
                    self.driver.execute_script("arguments[0].scrollIntoView(true);", navbar)
                    # Clica no botão usando JavaScript
                    self.driver.execute_script("arguments[0].click();", navbar)
                    print("Anúncio ignorado com sucesso.")
                except (NoSuchElementException, ElementNotInteractableException) as e:
                    print(f"Erro ao tentar clicar no botão de fechar anúncio: {e}")
        except TimeoutException:
            print("Nenhum anúncio encontrado ou já ignorado.")
        except NoSuchElementException:
            print("Elemento do anúncio não encontrado.")
        except Exception as e:
            print(f"Ocorreu um erro inesperado ao tentar ignorar anúncios: {e}")

# Utilização do método em seu teste
page = PageWithAds(driver)
page.ignore_ads()

# Remover anúncios via JavaScript (opcional)
def remove_ads_via_js(driver, elemento):
    try:
        # Exemplo: remover elementos com a classe 'ad-class' (ajuste conforme necessário)
        ads = driver.find_elements(By.XPATH, elemento)
        for ad in ads:
            driver.execute_script("arguments[0].remove();", ad)
        print("Anúncios removidos via JavaScript.")
    except Exception as e:
        print(f"Erro ao tentar remover anúncios via JavaScript: {e}")

remove_ads_via_js(driver)

#https://demoqa.com/webtables
# Continuar com o resto da sua automação
"//div[contains(@class,'ns-vzj1q-e-1 row-container canvas')]"
try:
    # Localizar o botão de iniciar a barra de progresso pelo ID correto
    start_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "startStopButton"))
    )
    # Rola até o botão
    driver.execute_script("arguments[0].scrollIntoView(true);", start_button)
    # Clica no botão
    start_button.click()
    print("Botão de iniciar clicado com sucesso.")
except TimeoutException:
    print("Botão de iniciar não encontrado, terminando execução.")
except NoSuchElementException:
    print("Botão de iniciar não encontrado, terminando execução.")
except ElementNotInteractableException:
    print("Botão de iniciar não interativo, terminando execução.")
except Exception as e:
    print(f"Ocorreu um erro inesperado ao interagir com o botão de iniciar: {e}")

# Aguardar alguns segundos para ver o resultado (opcional)
time.sleep(5)

# Fechar o navegador
driver.quit()


driver.save_full_page_screenshot
