# 📅 S.A.C.O – Sistema de Agendamento Claro e Objetivo

Sistema de agendamento simples e eficiente, desenvolvido com FastAPI e SQLite, com autenticação JWT e cobertura de testes com Pytest.

## 🚀 Tecnologias Utilizadas

- [Python 3.10+](https://www.python.org/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [Uvicorn](https://www.uvicorn.org/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [SQLite](https://www.sqlite.org/)
- [PyJWT](https://pyjwt.readthedocs.io/)
- [Pytest](https://docs.pytest.org/)

## 📂 Estrutura do Projeto

```bash
app/
├── main.py                  # Inicialização da API
├── database.py              # Conexão com o banco SQLite
├── models.py                # Definição das tabelas (User, Agendamento)
├── schemas.py               # Pydantic: Entrada/Saída dos dados
├── crud.py                  # Lógica de criação, leitura, edição e exclusão
├── auth.py                  # Criação e verificação de JWT
└── routers/
    ├── users.py             # Rotas de cadastro e login
    └── agendamentos.py      # Rotas de CRUD de agendamentos
tests/
├── test_users.py            # Testes de cadastro/login
└── test_agendamentos.py     # Testes de agendamentos

README.md                    # Este arquivo
requirements.txt             # Dependências do projeto
```

## ✅ Funcionalidades

### Usuários
- Cadastro de usuário com nome, e-mail (único) e senha (mínimo 6 caracteres)
- Autenticação via JWT (login)
- Proteção de rotas autenticadas

### Agendamentos
- Criar agendamento com data, hora, local e descrição
- Listar agendamentos por:
  - Data específica
  - Período (ex: semana, mês)
  - Local ou palavra-chave
- Editar ou excluir agendamentos futuros
- Validação para evitar conflitos no mesmo dia/horário

## 🔒 Autenticação

- JWT Token (Bearer Token)
- Após login, inclua o token no header das requisições:
```http
Authorization: Bearer <token>
```

## ▶️ Como Executar Localmente

### 1. Clone o projeto
```bash
git clone https://github.com/ErickSantos2002/S.A.C.O.git
cd S.A.C.O
```

### 2. Crie e ative o ambiente virtual
```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

### 3. Instale as dependências
```bash
pip install -r requirements.txt
```

### 4. Rode a aplicação
```bash
uvicorn app.main:app --reload
```

### 5. Acesse a documentação automática
- [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 🧪 Rodando os Testes

```bash
pytest tests/
```

---

## 📌 Requisitos do Sistema

- Python 3.10 ou superior
- SQLite para banco local
- FastAPI como framework principal
- Estrutura RESTful
- Cobertura de testes com Pytest

---

## 📃 Licença

Este projeto é livre para uso acadêmico e educacional.

---

## ✍️ Autor

Desenvolvido por Erick Santos – Projeto S.A.C.O 2025
