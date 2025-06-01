"""
routers/users.py
-----------------
Define as rotas da API para cadastro e login de usuários.
"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer
from app import models
from .. import schemas, crud, auth
from ..database import SessionLocal
from jose import jwt, JWTError
from ..auth import SECRET_KEY, ALGORITHM

router = APIRouter(prefix="/usuarios", tags=["Usuários"])
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="usuarios/login")

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

# autenticar usuário e obter id
def get_current_user_id(token: str = Depends(oauth2_scheme)) -> int:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email = payload.get("sub")
        if not email:
            raise HTTPException(status_code=401, detail="Token inválido")
    except JWTError:
        raise HTTPException(status_code=401, detail="Token inválido")

    db = SessionLocal()
    user = db.query(models.User).filter_by(email=email).first()
    if not user:
        raise HTTPException(status_code=401, detail="Usuário não encontrado")
    return user.id

# ✅ NOVA ROTA: lista todos os usuários
@router.get("/", response_model=list[schemas.UserOut])
def listar_usuarios(db: Session = Depends(get_db)):
    return db.query(models.User).all()