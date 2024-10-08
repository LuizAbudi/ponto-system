i
# Automação de Apontamento de Horas com Google Sheets

Este projeto implementa a automação de apontamento de horas. O projeto foi desenvolvido em Python e utiliza de uma integração com o Google Sheets para obter as informações das horas trabalhadas. Foi utilizado o framework `Selenium` para a automação do navegador e a biblioteca `google-api-python-client` para a integração com o Google Sheets.

## Observações Importantes

  - O projeto foi desenvolvido para um cenário específico, onde a planilha de horas é preenchida com o `Data`, `Código da Tarefa` (Obtido no sistema de registro das tarefas), `Horário de início da tarefa`, `Hora de término da tarefa`, `Descrição da tarefa`, `Apontado`. Caso a planilha seja diferente, é necessário alterar o código para se adequar ao novo cenário.

  - No código é adicionada a diferença de segundos para registro das tarefas no sistema. Na planilha coloque apenas horas e minutos.

  - O Código busca apenas as tarefas que não foram registradas no sistema, controlado pela coluna `Apontado` na planilha. Mantenha a coluna `Apontado` atualizada para que o código funcione corretamente.

  - **OBS**: Para que funcione corretamente, **é necessário que não haja registros de horas no sistema no dia da tarefa**, pois pode ocorrer de não conseguir inserir a tarefa no sistema por conta da diferença de segundos.

## Documentação
- [Python](https://docs.python.org/pt-br/3/)
- [Documentação Google](https://developers.google.com/sheets/api/quickstart/python?hl=pt-br)
- [Selenium](https://www.selenium.dev/pt-br/documentation/)

## Requisitos
  
  - [Python](https://www.python.org/downloads/)
  - [pip](https://pip.pypa.io/en/stable/getting-started/)
  - [Google Chrome](https://www.google.com/intl/pt-BR/chrome/)
  - Template Planilha Google

## Planilha 

  - A planilha deve conter as seguintes colunas:
      - Data
      - Codigo Tarefa Task
      - Descrição
      - Hora Início
      - Hora Fim
      - Total de Horas
      - Apontado
      - hora inicio formatada
      - hora fim formatada

  - **Entre na planilha de horas e clique em `Arquivo` -> `Fazer uma cópia` para copiar a planilha para a sua conta do Google.**

  - Com a cópia da planilha criada, clique em `Compartilhar` no canto superior direito, coloque como `Qualquer pessoa com o link`, em acessor `Acesso geral` selecione `Leitor`, em seguida copie o id da planilha e cole no arquivo `.env` na variável `GOOGLE_SPREADSHEET_ID`.
    - Na URL: docs.google.com/spreadsheets/d/`id_da_planilha`/edit#gid=0

  - Caso necessite adicionar mais colunas para as tarefas, clique com o botão direito na última linha do dia e clique em `Insira 1 linha acima`, em seguida copie e cole a última linha na nova linha criada. Dessa forma a nova linha terá as fórmulas necessárias para o cálculo das horas e apontamentos.

### Exemplo de uso da Planilha
<img src="https://ibb.co/Ws9jQsJ
" alt="Exemplo planilha">

## Credenciais Google

- Obter o arquivo `credentials.json` na [página de credenciais do Google](https://console.developers.google.com/apis/credentials). 
    - Clique em `Api e Serviços` -> `Credenciais` -> `Criar Credenciais` -> `Conta de serviço` -> `Colocar o nome da conta do serviço` -> `Concluir` -> `Entrar na conta de serviço` -> `Adicionar chave` -> `JSON`
    - Geralmente o arquivo é baixado automaticamente, caso não, clique em adicionar chave e selecione o tipo JSON.
    - Faça o download do arquivo e coloque na pasta `/config` com o nome `credentials.json`.
    - O arquivo de credentials deve ter os mesmos campos do arquivo `credentials.example.json`.
    - [Passo a passo](https://drive.google.com/drive/folders/17Xyg-GNeaCgPdQopkS7G0YwDtqcSord-?usp=drive_link)

- Após obter as credenciais, ative a API do Google Sheets.
  - Acesse a [página de APIs do Google Sheets](https://console.cloud.google.com/marketplace/product/google/sheets.googleapis.com?q=search&referrer=search&project=projeto-ponto-437319) e clique em ativar.



## Execução

### **Antes de seguir com o passo a seguir tenha garantia de que os passos anteriores foram realizados.**

OBS: Para a execução dos passos a seguir, é necessário ter o Python e o pip instalado na máquina. Caso não consiga ativar o `venv` os pacotes podem ser instalados globalmente.

<details>
  <summary style="font-size: 18px;">Passo 1: Criar e Ativar Ambiente Virtual</summary>
  
  Para executar o projeto, clone o repositório, pelo terminal, entre na pasta do projeto e execute o comando:

  ```bash
  python -m venv venv
  ```

  No Windows:

  ```bash
  venv\Scripts\activate
  ```

  No macOS/Linux:

  ```bash
  source venv/bin/activate
  ```

  Verificar se apareceu `(venv)` antes do local de trabalho no terminal:

</details>

<details>
  <summary style="font-size: 18px;">Passo 2: Criar o arquivo .env</summary>
  
  **Crie o arquivo `.env` na raiz do projeto e adicione as seguintes variáveis de ambiente:**

  ```bash
  GOOGLE_SPREADSHEET_ID="id_da_planilha"
  # Mudar de acordo com o sistema operacional
  CHROME_PATH="C:/Program Files/Google/Chrome/Application/chrome.exe"
  TASK_URL="url_do_sistema_de_tarefas"
  TASK_USER="usuario_do_sistema_de_tarefas"
  TASK_PASSWORD="senha_do_sistema_de_tarefas"
  ```

  - Para obter o caminho do Google Chrome no Linux, execute o comando `which google-chrome` no terminal. No Windows, o caminho padrão é `C:/Program Files/Google/Chrome/Application/chrome.exe`.
    - Garanta que o caminho do Chrome esteja correto, caso contrário, o script não irá funcionar.

  - O Id da planilha pode ser obtido na URL da planilha do Google Sheets:
    - docs.google.com/spreadsheets/d/`id_da_planilha`/edit#gid=0

</details>

<details>
  <summary style="font-size: 18px;">Passo 3: Executar o script</summary>

  Execute o comando para instalar as dependências:
  
  ```bash	
  pip install -r requirements.txt
  ```
  
  Em seguida, execute o comando:

  ```bash
  python main.py
  ```

  - Selecione o mês de referência para o apontamento de horas no terminal.
  - O navegador será aberto e o script irá preencher as tarefas no sistema de registro de tarefas.

</details>

---

### Considerações Finais

  - Apesar de ser um processo um pouco demorado para configurar, a automação de tarefas é uma ótima forma de otimizar o tempo. 
  - A integração com o Google Sheets é uma ótima forma de manter as informações das tarefas e sempre ter um backup das informações.
  - O tempo de preencher a planilha e a de registrar as tarefas no sistema pode não ser diferente, mas a automação é um facilitador para registrar os apontamentos, que as vezes podem ser esquecidos e quando acumulados podem gerar um gasto de tempo maior. 
