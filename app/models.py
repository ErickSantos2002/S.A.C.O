"""
models.py
----------
Define o modelo de dados (User) usado com SQLAlchemy para criar a tabela no banco de dados.
-------------------------
Adiciona a tabela Agendamento ao modelo existente.
"""

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    senha_hash = Column(String, nullable=False)

class Agendamento(Base):
    __tablename__ = "agendamentos"

    id = Column(Integer, primary_key=True, index=True)
    data_hora = Column(DateTime, nullable=False)
    local = Column(String, nullable=False)
    descricao = Column(String, nullable=True)
    motivo_cancelamento = Column(String, nullable=True)

    usuario_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    # Relacionamento com o usuário (1:N)
    usuario = relationship("User", backref="agendamentos")