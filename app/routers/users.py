"""
routers/users.py
-----------------
Define as rotas da API para cadastro e login de usuários.
"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import schemas, crud, auth
from ..database import SessionLocal

router = APIRouter(prefix="/usuarios", tags=["Usuários"])

# Dependência para pegar a sessão do banco em cada requisição
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/cadastro", response_model=schemas.UserOut)
def cadastrar_usuario(usuario: schemas.UserCreate, db: Session = Depends(get_db)):
    """
    Rota de cadastro. Retorna erro 400 se o e-mail já estiver cadastrado.
    """
    try:
        return crud.criar_usuario(db, usuario)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/login")
def login(usuario: schemas.UserLogin, db: Session = Depends(get_db)):
    """
    Rota de login. Retorna o JWT se o usuário for autenticado.
    """
    user = crud.autenticar_usuario(db, usuario.email, usuario.senha)
    if not user:
        raise HTTPException(status_code=401, detail="Credenciais inválidas")
    token = auth.criar_token({"sub": user.email})
    return {"access_token": token, "token_type": "bearer"}
