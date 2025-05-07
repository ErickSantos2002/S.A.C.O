"""
database.py
------------
Responsável por configurar a conexão com o banco de dados SQLite
e criar a base para o SQLAlchemy trabalhar com ORM.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Caminho do banco de dados SQLite local
DATABASE_URL = "sqlite:///./saco.db"

# Criação do engine para se conectar ao banco
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Cria sessões do banco para uso com o SQLAlchemy
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

# Base para os modelos (tabelas)
Base = declarative_base()
