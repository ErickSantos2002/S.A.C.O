"""
main.py
--------
Ponto de entrada da aplicação. Inicializa o FastAPI e inclui as rotas.
---------------------
Inclui as rotas de agendamentos ao lado de usuários.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database import Base, engine
from .routers import users, agendamentos
from . import models

# Criação das tabelas
Base.metadata.create_all(bind=engine)

app = FastAPI(title="S.A.C.O - Agendamentos")

# Permite requisições de qualquer origem (ideal para testes locais)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Em produção, substitua "*" pelo domínio do frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Inclusão das rotas
app.include_router(users.router)
app.include_router(agendamentos.router)
