from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

class SiteInteraction:
    def __init__(self):
        chrome_options = Options()
        chrome_options.binary_location = "/mnt/c/Program Files/Google/Chrome/Application/chrome.exe"
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-gpu")

        try:
            print("Iniciando Chrome...")
            self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
            print("Chrome iniciado com sucesso.")
        except Exception as e:
            print(f"Error starting Chrome: {e}")
            self.driver = None

    def access_site(self, url):
        if self.driver:
            self.driver.get(url)
            time.sleep(2)
        else:
            print("Driver não está disponível. Não foi possível acessar o site.")

    def click_button(self, selector):
        if self.driver:
            try:
                button = self.driver.find_element(By.CSS_SELECTOR, selector)
                button.click()
                time.sleep(1)
            except Exception as e:
                print(f"Error clicking button: {selector}, {e}")
        else:
            print("Driver não está disponível. Não foi possível clicar no botão.")

    def clear_input(self, input_selector):
        if self.driver:
            try:
                input_field = self.driver.find_element(By.CSS_SELECTOR, input_selector)
                input_field.clear()
            except Exception as e:
                print(f"Error clearing input: {input_selector}, {e}")
        else:
            print("Driver não está disponível. Não foi possível limpar o campo.")

    def enter_text(self, input_selector, text):
        if self.driver:
            try:
                input_field = self.driver.find_element(By.CSS_SELECTOR, input_selector)
                input_field.send_keys(text)
            except Exception as e:
                print(f"Error entering text in input: {input_selector}, {e}")
        else:
            print("Driver não está disponível. Não foi possível inserir texto.")

    def wait_for_message(self, message):
        if self.driver:
            timeout = 10
            while timeout > 0:
                try:
                    success_message = self.driver.find_element(By.XPATH, f"//div[contains(text(), '{message}')]")
                    return success_message.text
                except Exception:
                    time.sleep(1)
                    timeout -= 1
            return None
        else:
            print("Driver não está disponível. Não foi possível esperar pela mensagem.")
            return None

    def process_entries(self, entries):
        print(entries)
        # for entry in entries:
        #     self.click_button("button[data-toggle='modal'][data-target='#modalExecucoes']")
            
        #     self.click_button("button[ng-click='incluirExecucao(ordemServicoEdicao)']")
            
        #     self.clear_input("#dhinicio")
        #     self.enter_text("#dhinicio", entry['dh_inicio'])

        #     self.clear_input("#dhtermino")
        #     self.enter_text("#dhtermino", entry['dh_fim'])
            
        #     self.enter_text("textarea[name='name']", entry['descricao'])
            
        #     self.click_button("button[ng-click='salvarExecucao(ordemServicoEdicao)']")
            
        #     success_message = self.wait_for_message("Execução Salva com Sucesso!")
        #     print(success_message)

    def close(self):
        if self.driver:
            self.driver.quit()
            print("Chrome fechado.")
        else:
            print("Driver não estava disponível. Não foi possível fechar.")