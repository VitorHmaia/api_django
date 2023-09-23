# API de Gerenciamento de Alunos, Disciplinas e Tarefas

Esta é uma API RESTful em Django desenvolvida para auxiliar os alunos no gerenciamento de suas disciplinas e tarefas.

## Tecnologias Utilizadas

- **Django**: O framework web Python usado como base para a API.
- **Django REST framework**: Uma extensão do Django que facilita a criação de APIs RESTful.
- **Banco de Dados**: A API utiliza um banco de dados para armazenar informações de alunos, disciplinas e tarefas.
- **RESTful**: A API segue os princípios do estilo arquitetural REST, o que significa que as operações são baseadas em URLs e métodos HTTP padrão.

## Funcionalidades Principais

A API oferece as seguintes funcionalidades:

- **Alunos**: Criação, listagem, atualização e exclusão de alunos.
- **Disciplinas**: Criação, listagem, atualização e exclusão de disciplinas.
- **Tarefas**: Criação, listagem, atualização e exclusão de tarefas associadas a alunos e disciplinas.
- **Relações**: Associação de tarefas a alunos e disciplinas.

## Uso da API

Siga os passos abaixo para rodar a API localmente e importar as coleções no Postman para testar as funcionalidades.

**Passo 1: Configuração do Ambiente**

1. Certifique-se de que você ativou seu ambiente virtual como explicado [aqui](#como-criar-e-ativar-o-ambiente-virtual).

**Passo 2: Instalação das Dependências**

1. No terminal, navegue até o diretório raiz do seu projeto Django.

2. Execute o seguinte comando para instalar as dependências:

    ```bash
    pip install -r requirements.txt
    ```

**Passo 3: Rodar a Aplicação Localmente**

1. Ainda no terminal, execute o seguinte comando para rodar a aplicação localmente:

    ```bash
    python manage.py runserver
    ```

   Isso iniciará o servidor de desenvolvimento da aplicação.

2. Acesse a API no seu navegador ou utilizando ferramentas como o [Postman](https://www.postman.com/).

**Passo 4: Importar Coleções no Postman**

1. Abra o Postman.

2. Clique em "Import" na barra de navegação esquerda.

3. Selecione a opção "Link" e cole o link da coleção de testes (se disponível).

4. Ou selecione a opção "Upload Files" e faça o upload do arquivo de coleção fornecido.

**Passo 5: Testar a API no Postman**

1. Na barra de navegação esquerda do Postman, você encontrará as coleções importadas.

2. Clique na coleção relevante e selecione o pedido que deseja testar.

3. Preencha os parâmetros necessários no pedido (por exemplo, corpo JSON) e clique em "Send" para fazer a solicitação à API.

4. Analise a resposta da API para verificar se tudo está funcionando conforme o esperado.

Certifique-se de ajustar os endpoints e os parâmetros de acordo com as necessidades do seu projeto.


