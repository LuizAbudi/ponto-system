# Automação de Apontamento de Horas com Google Sheets

Este projeto implementa a automação de apontamento de horas. O projeto foi desenvolvido em Python e utiliza de uma integração com o Google Sheets para obter as informações das horas trabalhadas. Foi utilizado o framework `Selenium` para a automação do navegador e a biblioteca `google-api-python-client` para a integração com o Google Sheets.

## Documentação
- [Python](https://docs.python.org/pt-br/3/)
- [Documentação Google](https://developers.google.com/sheets/api/quickstart/python?hl=pt-br)
- [Selenium](https://www.selenium.dev/pt-br/documentation/)


## Requisitos

- [Python](https://www.python.org/downloads/)
- [Google Chrome](https://www.google.com/intl/pt-BR/chrome/)
- Template Planilha Google


### Execução

Para executar o projeto, clone o repositório, pelo terminal, entre na pasta do projeto e execute o comando:

```bash	
pip install -r requirements.txt
```

**Crie o arquivo `.env` na raiz do projeto e adicione as seguintes variáveis de ambiente:**

```bash
GOOGLE_SPREADSHEET_ID="id_da_planilha"
# Mudar de acordo com o sistema operacional
CHROME_PATH="C:/Program Files/Google/Chrome/Application/chrome.exe"
TASK_URL="url_do_sistema_de_tarefas"
TASK_USER="usuario_do_sistema_de_tarefas"
TASK_PASSWORD="senha_do_sistema_de_tarefas"
```

- O Id da planilha pode ser obtido na URL da planilha do Google Sheets:
  - docs.google.com/spreadsheets/d/`id_da_planilha`/edit#gid=0

**Obtendo as credenciais para acesso à planilha**

- Obter o arquivo `credentials.json` na [página de credenciais do Google](https://console.developers.google.com/apis/credentials). 
  - Clique em `Api e Serviços` -> `Credenciais` -> `Criar Credenciais` -> `Conta de serviço` -> `Colocar o nome da conta do serviço` -> `Concluir` -> `Entrar na conta de serviço` -> `Adicionar chave` -> `JSON`
  - Faça o download do arquivo e coloque na pasta `/config` com o nome `credentials.json`.
  - O arquivo de credentials deve ter os mesmos campos do arquivo `credentials.example.json`.
  - [Passo a passo](https://drive.google.com/drive/folders/17Xyg-GNeaCgPdQopkS7G0YwDtqcSord-?usp=drive_link)

Em seguida, execute o comando:

```bash
python main.py
```

- Selecione o mês de referencia para o apontamento de horas no terminal.

- O navegador será aberto e o script irá preencher as tarefas no sistema de registro de tarefas.

## Observações Importantes
- O projeto foi desenvolvido para um cenário específico, onde a planilha de horas é preenchida com o `Data`, `Código da Tarefa` (Obtido no sistema de registro das tarefas), `Horário de inicio da tarefa`, `Hora de término da tarefa`, `Descrição da tarefa`, `Apontado`. Caso a planilha seja diferente, é necessário alterar o código para se adequar ao novo cenário.

- No código é adicionado a diferença de segundos para registro das tarefas no sistema. Na planilha coloque apenas horas e minutos.

- O Código busca apenas as tarefas que não foram registradas no sistema, controlado pela coluna `Apontado` na planilha. Mantenha a coluna `Apontado` atualizada para que o código funcione corretamente.

- **OBS**: Para que funcione corretamente, **é necessário que não tenha registros de horas no sistema no dia da tarefa**, pois pode ocorrer de não conseguir inserir a tarefa no sistema por conta da diferença de segundos.


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

- Com a cópia da planilha criada clique em `Compartilhar` no canto superior direito, coloque como `Qualquer pessoa com o link`, em acessor `Acesso geral` selecione `Leitor`, em seguida copie o id da planilha e cole no arquivo `.env` na variável `GOOGLE_SPREADSHEET_ID`.
  - Na URL: docs.google.com/spreadsheets/d/`id_da_planilha`/edit#gid=0

- Caso necessite adicionar mais colunas para as tarefas, clique com o botão direito na ultima linha do dia e clique em `Insira 1 linha acima`, em seguida copie e cole a ultima linha na nova linha criada. Dessa forma a nova linha terá as fórmulas necessárias para o cálculo das horas e apontamentos.

---

### Considerações Finais

  - Apesar de ser um processo um pouco demorado para configurar, a automação de tarefas é uma ótima forma de otimizar o tempo. 
  - A integração com o Google Sheets é uma ótima forma de manter as informações das tarefas e sempre ter um backup das informações.
  - O tempo de preencher a planilha e a de registrar as tarefas no sistema pode não ser diferente, mas a automação é um facilitador para registrar os apontamentos, que as vezes podem ser esquecidos e quando acumulados podem gerar um gasto de tempo maior. 
