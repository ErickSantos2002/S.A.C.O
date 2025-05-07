"""
main.py
--------
Ponto de entrada da aplicação. Inicializa o FastAPI e inclui as rotas.
---------------------
Inclui as rotas de agendamentos ao lado de usuários.
"""

from fastapi import FastAPI
from .database import Base, engine
from .routers import users, agendamentos

# Criação das tabelas
Base.metadata.create_all(bind=engine)

app = FastAPI(title="S.A.C.O - Agendamentos")

# Inclusão das rotas
app.include_router(users.router)
app.include_router(agendamentos.router)
