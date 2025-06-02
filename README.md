# Projeto E-commerce Django

Este é um projeto básico de e-commerce desenvolvido com Django, focado na gestão de produtos com operações CRUD (Criar, Ler, Atualizar, Deletar).

## Estrutura do Projeto
O projeto consiste em:

- **loja_produtos**: projeto principal Django
- **produtos**: aplicação que gerencia o cadastro de produtos

## Requisitos
- Python 3.10 ou superior
- Django 5.2

## Configuração do Ambiente
1. Clone o repositório
    ```bash
    git clone https://github.com/KateMorf/backend-django.git
    cd backend-django
    ```

2. Crie e ative um ambiente virtual
    ```bash
    # Windows
    python -m venv venv
    venv\Scripts\activate

    # Linux/Mac
    python -m venv venv
    source venv/bin/activate
    ```

3. Instale as dependências
    ```bash
    pip install -r requirements.txt
    # ou
    pip install django==5.2
    ```

4. Configure o banco de dados
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5. Crie um superusuário para acessar o admin
    ```bash
    python manage.py createsuperuser
    ```

6. Inicie o servidor de desenvolvimento
    ```bash
    python manage.py runserver
    ```

Acesse o projeto em: http://127.0.0.1:8000/

## Funcionalidades
- **Listagem de Produtos**: Navegue pela lista de produtos cadastrados
- **Criação de Produtos**: Adicione novos produtos ao catálogo
- **Edição de Produtos**: Atualize informações dos produtos existentes
- **Remoção de Produtos**: Exclua produtos do catálogo

## Rotas
- `/`: Lista todos os produtos
- `/novo/`: Formulário para criar um novo produto
- `/edita/<id>/`: Formulário para editar um produto existente
- `/remove/<id>/`: Confirma a remoção de um produto
- `/admin/`: Interface de administração

## Estrutura de Arquivos
O projeto segue a estrutura padrão do Django:

- **models.py**: Define o modelo de dados Produto
- **views.py**: Contém a lógica das views para as operações CRUD
- **forms.py**: Define o formulário para criação/edição de produtos
- **urls.py**: Mapeia URLs para as views correspondentes
- **templates/**: Contém os templates HTML

## Administração
Para acessar a área administrativa:

1. Acesse http://127.0.0.1:8000/admin/
2. Faça login com as credenciais do superusuário criado anteriormente

A partir dali você poderá gerenciar produtos, usuários e outros aspectos do sistema.

Este é um projeto básico de e-commerce desenvolvido com Django, focado na gestão de produtos com operações CRUD (Criar, Ler, Atualizar, Deletar).


