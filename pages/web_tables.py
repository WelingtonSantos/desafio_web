# Página com a classe webtables
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from faker import Faker

fake = Faker()
EMAIL = ' '
class WebTables():
    """Classe web tables preenchendo o formulário"""
    
    def __init__(self, driver):
        self.driver = driver        
        self.formulario = "//div[@class='modal-title h4'][contains(.,'Registration Form')]"
        self.titulo = "Registration Form"
        self.primeiro_nome = "//input[contains(@placeholder,'First Name')]"
        self.ultimo_nome = "//input[contains(@placeholder,'Last Name')]"
        self.e_mail = "//input[contains(@id,'userEmail')]"
        self.idade = "//input[contains(@id,'age')]"
        self.salario = "//input[contains(@id,'salary')]"
        self.departamento = "//input[contains(@placeholder,'Department')]"
        self.enviar = "//button[@type='submit'][contains(.,'Submit')]"
        self.pop_up ="//div[contains(@class,'ns-vzj1q-e-1 row-container canvas')]"
        self.consulta = "//input[contains(@autocomplete,'off')]"
    
    def form(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(
        (By.XPATH, self.formulario)))

        
    
    def first_name(self): 
        self.driver.execute_script("document.querySelector('iframe').remove();")       
        name = fake.unique.first_name()
        elemento = self.driver.find_element(By.XPATH, self.primeiro_nome)
        elemento.send_keys(name)
    
    def last_name(self):
        last_name = fake.unique.last_name()
        elemento = self.driver.find_element(By.XPATH, self.ultimo_nome)
        elemento.send_keys(last_name)
        self.driver.save_screenshot('last_name.png')
    
    def email(self):
        email = fake.email()
        elemento = self.driver.find_element(By.XPATH, self.e_mail)
        elemento.send_keys(email)
    
    def data_nascimento(self):
        data_nascimento = 20
        elemento = self.driver.find_element(By.XPATH, self.idade)
        elemento.send_keys(data_nascimento)
        
    
    def salario_base(self):
        salario = 1000
        elemento = self.driver.find_element(By.XPATH, self.salario)
        elemento.send_keys(salario)
        
        
    def departament(self):
        area = "Tecnologia"
        elemento = self.driver.find_element(By.XPATH, self.departamento)
        elemento.send_keys(area)
        
    
    def enviar_formulario(self):
        elemento = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.enviar))
        )
        self.driver.execute_script("arguments[0].click();", elemento)                    
        #elemento.click()
    
    def get_cadastro(self):
        
        consulta =self.driver.find_element(By.XPATH, self.consulta)
        consulta.send_keys("Tecnologia")
        self.driver.save_screenshot('formulairo.png')
        
        
    
    # Remover anúncios via JavaScript (opcional)
    def remove_ads_via_js(self):
        try:   
            ads = self.driver.find_elements(By.XPATH, self.pop_up)
            for ad in ads:
                self.driver.execute_script("arguments[0].remove();", ad)
        except Exception as e:
            print(f"Erro ao tentar remover anúncios via JavaScript: {e}")
    

    
        
    
        