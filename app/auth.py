"""
auth.py
--------
Contém funções para hash de senha, verificação e geração de tokens JWT.
"""

from passlib.context import CryptContext
from jose import JWTError, jwt
from datetime import datetime, timedelta

# SEGREDO – importante mover para .env em produção
SECRET_KEY = "secreto_muito_seguro"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

# Criptografia para senhas
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def criar_hash(senha: str) -> str:
    """Retorna o hash da senha usando bcrypt"""
    return pwd_context.hash(senha)

def verificar_senha(senha: str, hash: str) -> bool:
    """Verifica se a senha bate com o hash armazenado"""
    return pwd_context.verify(senha, hash)

def criar_token(dados: dict):
    """Gera um JWT com os dados informados"""
    dados_copia = dados.copy()
    expira = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    dados_copia.update({"exp": expira})
    return jwt.encode(dados_copia, SECRET_KEY, algorithm=ALGORITHM)
