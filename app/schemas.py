"""
schemas.py
-----------
Define os esquemas (modelos de entrada e saída de dados) usados para validação com Pydantic.
-------------------------
Esquemas de entrada e saída de dados para agendamentos.
"""

from pydantic import BaseModel, EmailStr, constr
from datetime import datetime

# Schema para cadastro de novo usuário
class UserCreate(BaseModel):
    nome: str
    email: EmailStr
    senha: constr(min_length=6)  # senha com no mínimo 6 caracteres

# Schema para login
class UserLogin(BaseModel):
    email: EmailStr
    senha: str

# Schema para retornar dados do usuário sem mostrar a senha
class UserOut(BaseModel):
    id: int
    nome: str
    email: EmailStr

    class Config:
        orm_mode = True  # Permite conversão automática de ORM para Pydantic

class AgendamentoBase(BaseModel):
    data_hora: datetime
    local: str
    descricao: str | None = None

class AgendamentoCreate(AgendamentoBase):
    pass

class AgendamentoOut(AgendamentoBase):
    id: int
    usuario_id: int
    motivo_cancelamento: str | None = None

    class Config:
        orm_mode = True

class Cancelamento(BaseModel):
    motivo: str

class UserOut(BaseModel):
    id: int
    nome: str
    email: EmailStr

    class Config:
        orm_mode = True