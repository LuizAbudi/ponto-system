import time
import sys

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys


class SiteInteraction:
    def __init__(self):
        chrome_options = Options()
        # Caminho para o Chrome
        chrome_options.binary_location = "C:/Program Files/Google/Chrome/Application/chrome.exe"
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-gpu")

        try:
            print("Iniciando Chrome...")
            self.driver = webdriver.Chrome(service=Service(
                ChromeDriverManager().install()), options=chrome_options)
            print("Chrome iniciado com sucesso.")
        except Exception as e:
            print(f"Erro ao iniciar o Chrome: {e}")
            self.driver = None

        if self.driver is None:
            print("Driver não está disponível. Finalizando execução.")
            sys.exit(1)

    def access_site(self, url):
        if self.driver:
            try:
                self.driver.get(url)
                time.sleep(2)
                print(f"Acessando o site: {url}")
            except Exception as e:
                print(f"Erro ao acessar o site {url}: {e}")
        else:
            print("Driver não disponível. Não foi possível acessar o site.")

    def login_in_site(self, url, user, password):
        self.driver.get(url)

        time.sleep(3)

        user_field = self.driver.find_element(By.ID, "usuario")
        user_field.clear()
        user_field.send_keys(user)

        password_field = self.driver.find_element(By.ID, "senha")
        password_field.clear()
        password_field.send_keys(password)

        login_button = self.driver.find_element(
            By.CSS_SELECTOR, "button.btn-login")
        login_button.click()

        time.sleep(5)

    def click_button(self, selector):
        if self.driver:
            try:
                button = self.driver.find_element(By.CSS_SELECTOR, selector)
                button.click()
                time.sleep(2)
                print(f"Botão clicado: {selector}")
            except Exception as e:
                print(f"Erro ao clicar no botão: {selector}. {e}")
        else:
            print("Driver não está disponível. Não foi possível clicar no botão.")

    def clear_input(self, input_selector):
        if self.driver:
            try:
                input_field = self.driver.find_element(
                    By.CSS_SELECTOR, input_selector)
                input_field.click()
                print(f"Clicado no campo: {input_selector}")

                input_field.send_keys(Keys.CONTROL + 'a')

                input_field.send_keys(Keys.BACKSPACE)
                print(f"Campo limpo: {input_selector}")
            except Exception as e:
                print(f"Erro ao limpar o campo: {input_selector}. {e}")
        else:
            print("Driver não está disponível. Não foi possível limpar o campo.")

    def enter_text(self, input_selector, text):
        if self.driver:
            try:
                input_field = self.driver.find_element(
                    By.CSS_SELECTOR, input_selector)
                input_field.send_keys(text)
                print(f"Texto inserido no campo {input_selector}: {text}")
            except Exception as e:
                print(f"Erro ao inserir texto no campo: {input_selector}. {e}")
        else:
            print("Driver não está disponível. Não foi possível inserir texto.")

    def wait_for_message(self, message):
        if self.driver:
            timeout = 10
            while timeout > 0:
                try:
                    success_message = self.driver.find_element(
                        By.XPATH, f"//div[contains(text(), '{message}')]")
                    return success_message.text
                except Exception:
                    time.sleep(1)
                    timeout -= 1
            return None
        else:
            print("Driver não está disponível. Não foi possível esperar pela mensagem.")
            return None

    def select_task(self, task):
        if self.driver:
            try:
                task_element = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located(
                        (By.XPATH, f"//th[normalize-space(text())='{task}']"))
                )

                task_row = task_element.find_element(
                    By.XPATH, './ancestor::tr')

                button = task_row.find_element(
                    By.XPATH, ".//button[@data-toggle='modal'][@data-target='#modalExecucoes']")

                button.click()

                print(f"Tarefa selecionada: {task}")
                print("Botão de execuções clicado.")
            except Exception as e:
                print(f"Erro ao selecionar a tarefa: {task}. {e}")
        else:
            print("Driver não está disponível. Não foi possível selecionar a tarefa.")

    def process_entries(self, entries):
        for entry in entries:
            print(f"Iniciando processamento da entrada: {entry}")
            try:
                self.select_task(entry['task'])

                self.click_button(
                    "button[ng-click='incluirExecucao(ordemServicoEdicao)']")
                print("Botão de incluir execução clicado.")

                self.clear_input("#dhinicio")
                self.enter_text("#dhinicio", entry['dh_inicio'])

                self.clear_input("#dhtermino")
                self.enter_text("#dhtermino", entry['dh_fim'])

                self.enter_text("textarea[name='name']", entry['descricao'])

                self.click_button(
                    "button[ng-click='salvarExecucao(ordemServicoEdicao)']")
                print("Execução salva.")

                self.click_button(
                    "button[ng-click='fecharExecucao(execucao)']")
                print("Execução fechada.")

                success_message = self.wait_for_message(
                    "Execução Salva com Sucesso!")
                if success_message:
                    print(f"Mensagem de sucesso recebida: {success_message}")
                else:
                    print("Mensagem de sucesso não encontrada.")

            except Exception as e:
                print(f"Erro ao processar entrada: {entry}. {e}")

            print('--------------------------------------')

    def close(self):
        if self.driver:
            self.driver.quit()
            print("Chrome fechado.")
        else:
            print("Driver não estava disponível. Não foi possível fechar.")
