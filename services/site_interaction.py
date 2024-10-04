import sys
import time

from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


class SiteInteraction:
    def __init__(self, chrome_path):
        chrome_options = Options()
        chrome_options.binary_location = chrome_path
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-gpu")

        try:
            print("Iniciando Chrome...")
            self.driver = webdriver.Chrome(service=Service(
                ChromeDriverManager().install()), options=chrome_options)
            print("Chrome iniciado com sucesso.")
        except WebDriverException as e:
            print(f"Erro ao iniciar o Chrome: {e}")
            self.driver = None
        except FileNotFoundError as e:
            print(f"Arquivo não encontrado: {e}")
            self.driver = None
        except Exception as e:
            print(f"Erro inesperado: {e}")
            self.driver = None

        if self.driver is None:
            print("Driver não está disponível. Finalizando execução.")
            sys.exit(1)

    def access_site(self, url):
        if self.driver:
            try:
                self.driver.get(url)
                time.sleep(2)
                print(f"Acessando o site: {url}\n")
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
                input_field.send_keys(Keys.CONTROL + 'a')

                input_field.send_keys(Keys.BACKSPACE)
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
            except Exception as e:
                print(f"Erro ao selecionar a tarefa: {task}. {e}")
        else:
            print("Driver não está disponível. Não foi possível selecionar a tarefa.")

    def process_entries(self, entries):
        for entry in entries:
            print(f"Iniciando processamento da entrada: {entry}\n")
            try:
                self.select_task(entry['task'])

                self.click_button(
                    "button[ng-click='incluirExecucao(ordemServicoEdicao)']")

                self.clear_input("#dhinicio")
                self.enter_text("#dhinicio", entry['dh_inicio'])

                self.clear_input("#dhtermino")
                self.enter_text("#dhtermino", entry['dh_fim'])

                self.enter_text("textarea[name='name']", entry['descricao'])

                self.click_button(
                    "button[ng-click='salvarExecucao(ordemServicoEdicao)']")

                self.click_button(
                    "button[ng-click='fecharExecucao(execucao)']")

                success_message = self.wait_for_message(
                    "Execução Salva com Sucesso!")
                if success_message:
                    print("Apontamento realizado:\n")
                    print(f"Tarefa: {entry['task']}\n")
                    print(f"Data e Hora de Início: {entry['dh_inicio']}\n")
                    print(f"Data e Hora de Fim: {entry['dh_fim']}\n")
                    print(f"Descrição: {entry['descricao']}\n")
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

    def execute(self, url, user, password, entries):
        self.access_site(url)
        self.login_in_site(url, user, password)
        self.process_entries(entries)
        self.close()
