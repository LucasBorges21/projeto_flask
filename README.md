# Projeto Flask - Sistema de Cadastro Simples

Este é um projeto em desenvolvimento com o objetivo de praticar e consolidar conhecimentos em **desenvolvimento web com Flask**, especialmente voltado para funcionalidades de **cadastro de usuários**, **manipulação de formulários com Flask-WTF** e **integração com banco de dados utilizando SQLAlchemy**.

## Funcionalidades atuais

- Página inicial básica (`/`)
- Página de cadastro de usuários (`/cadastro`) com:
  - Formulário validado com Flask-WTF
  - Armazenamento dos dados no banco de dados via SQLAlchemy

## Tecnologias utilizadas

- Python 3.x  
- Flask  
- Flask-WTF  
- SQLAlchemy  
- SQLite (ou outro banco relacional configurado)

## Estrutura do projeto
PROJETO_FLASK/
│
├── app/
│ ├── static/ # Arquivos estáticos (CSS, JS, imagens)
│ │ ├── css/
│ │ ├── img/
│ │ │ └── logo.png
│ │ └── js/
│ ├── templates/ # Templates HTML com Jinja2
│ │ ├── index.html
│ │ └── cadastro.html
│ ├── init.py # Inicialização da aplicação Flask
│ ├── forms.py # Formulários com Flask-WTF
│ ├── models.py # Definição de tabelas com SQLAlchemy
│ └── routes.py # Rotas da aplicação
│
├── instance/ # Configurações específicas por ambiente
│
├── migrations/ # Mapeamento de versões do banco (Flask-Migrate)
│
├── main.py # Arquivo de entrada da aplicação
├── .gitignore # Arquivos/ pastas ignorados pelo Git
