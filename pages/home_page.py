from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.alerts_frames_windows_xpath = "//h5[text()='Alerts, Frame & Windows']"
        self.page_locator = '/html/body/div[2]/div/div/div[2]/div/div[3]/div/div[3]'
        self.elements_locator = "//h5[contains(.,'Elements')]"

    def open_home_page(self):
        self.driver.get("https://demoqa.com")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def click_alerts_frames_windows(self):
        elemento = self.driver.find_element(By.XPATH, self.page_locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", elemento)
        elemento.click()

    def wait_for_page_load(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(
            (By.XPATH, self.alerts_frames_windows_xpath)))

    def menu_elements(self):
        elemento = self.driver.find_element(By.XPATH, self.elements_locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", elemento)
        elemento.click()
        
        