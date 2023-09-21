# API Django
Este repositório é destinado a postagem da api em python desenvolvida conforme solicitado em sala de aula.

# Guia de Configuração e Execução da Aplicação Django

Este guia fornecerá instruções passo a passo sobre como configurar e executar a aplicação Django. Certifique-se de seguir todas as etapas cuidadosamente para garantir que a aplicação funcione corretamente.

## Requisitos Prévios

1. **Python**: A aplicação Django é baseada em Python. Certifique-se de ter o Python instalado. Você pode verificar a versão do Python instalada executando o comando `python --version` no terminal.

2. **Banco de Dados**: Verifique se você possui um banco de dados compatível instalado e configurado. O Django suporta vários bancos de dados, como PostgreSQL, MySQL, SQLite, entre outros.

3. **Virtualenv (Opcional)**: É recomendável criar um ambiente virtual para isolar as dependências da aplicação. Você pode instalar o `virtualenv` usando o seguinte comando: pip install virtualenv

## Configuração Inicial

Siga estas etapas para configurar a aplicação:

1. Clone o repositório para o seu ambiente local:
git clone <URL do Repositório>


2. Navegue até o diretório da aplicação:
cd <diretório-da-aplicação>


3. Crie um ambiente virtual (opcional, mas recomendado):
virtualenv venv .env


4. Ative o ambiente virtual:

- No Windows:

  ```
  venv\Scripts\activate
  ```

- No macOS e Linux:

  ```
  source venv/bin/activate
  ```

5. Instale as dependências da aplicação:
pip install -r requirements.txt


## Configuração do Banco de Dados

1. Configure as configurações do banco de dados no arquivo `settings.py` da aplicação. Certifique-se de definir as credenciais corretas e o tipo de banco de dados que você está usando.

2. Execute as migrações do banco de dados:
python manage.py migrate


## Iniciar a Aplicação

Agora que a aplicação está configurada, você pode iniciá-la:

1. Execute o servidor de desenvolvimento:
python manage.py runserver


2. Acesse a aplicação em seu navegador da web:
http://localhost:8000/

3. Importe o arquivo 'API testes- CRUD.postman_collection' no Postman para testar as requisições e repostas.








