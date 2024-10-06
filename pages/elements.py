# Página com a classe elements
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Element():
    """Essa classe representa a pagina element"""
    def __init__(self, driver):
        self.driver = driver
        self.menu = "//div[@class='header-text'][contains(.,'Elements')]"
        self.web_tables = "//li[@class='btn btn-light '][contains(.,'Web Tables')]"
        self.add_button = "//button[@type='button'][contains(.,'Add')]"
         
    def element_page(self):
        self.driver.get("https://demoqa.com/elements")
    
    def wait_for_page_load(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(
        (By.XPATH, self.menu)))
    
    def web_table_click(self):
        elemento = self.driver.find_element(By.XPATH, self.web_tables)
        elemento.click()
        self.driver.implicitly_wait(10)
    
    def add_button_click(self):
        elemento = self.driver.find_element(By.XPATH, self.add_button)
        elemento.click()
    
    # Remover anúncios via JavaScript (opcional)
    def remove_ads_via_js(self, elemento):
        try:
        # Exemplo: remover elementos com a classe 'ad-class' (ajuste conforme necessário)
            ads = self.driver.find_elements(By.XPATH, elemento)
            for ad in ads:
                self.driver.execute_script("arguments[0].remove();", ad)           
        except Exception as e:
            print(f"Erro ao tentar remover anúncios via JavaScript: {e}")
    

        