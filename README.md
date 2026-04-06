# Temporal Workflow Project

Este projeto utiliza o [Temporal](https://temporal.io/) para orquestrar fluxos de trabalho e atividades de manipulação de dados, integrando a geração de dados simulados (fake data) em CSV e o carregamento desses dados para o MongoDB.

## Descrição do Projeto

O projeto consiste em um Workflow gerenciado pelo Temporal e algumas "Activities" associadas para tarefas pesadas ou que envolvem chamadas de banco de dados e arquivos locais:
1. **Atividade 1 (`generate_csv_activity`)**: Executa um script Python que utiliza a biblioteca `faker` e `pandas` para gerar um arquivo CSV.
2. **Atividade 2 (`load_to_mongo`)**: Lê o CSV recém-criado, formata e insere os dados gerados dentro de um banco de dados MongoDB na nuvem ou localmente através de uma URI definida via `.env`.

## Pré-requisitos

Certifique-se de que o seu ambiente possua as seguintes tecnologias instaladas ou em funcionamento:
* **Python 3.8+**
* **MongoDB** (Rodando local ou via MongoDB Atlas)
* **Temporal Server** (Serviço de desenvolvimento do Temporal devidamente iniciado na porta **8081**).

## Instalação

Clone este repositório em sua máquina:

```bash
git clone <url-do-repositorio>
cd atvd_02
```

Instale as dependências (por exemplo, dentro de um virtualenv):

```bash
pip install temporalio pandas pymongo python-dotenv faker
```

Crie um arquivo `.env` na raiz do projeto contendo as rotas e senhas do MongoDB. Exemplo:

```env
MONGODB_URI=mongodb://localhost:27017/
MONGODB_DATABASE=dataops_lab
MONGODB_COLLECTION=orders_raw
```

## Como configurar o Temporal Server

O código foi atualizado para se conectar ao Temporal na porta **8081**. Caso utilize a CLI do Temporal, inicie o servidor com a porta especificada:

```bash
temporal server start-dev --port 8081
```

## Utilização

Todas as execuções de comandos devem partir do diretório raiz do projeto e referenciar o módulo `app`.

Para iniciar o Worker do Temporal, ele ficará disponível à espera dos jobs a serem processados:
```bash
python -m app.worker
```

Em um terminal separado, você pode acionar ou visualizar a chamada do Workflow executando o script de ativação:
```bash
python -m app.run_workflow
```

O Workflow orquestrará a criação dos dados em formato CSV, em seguida passará o caminho do arquivo para o Worker respectivo carregar esses dados nas collections do MongoDB de acordo com o arquivo `.env`.
