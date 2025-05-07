"""
routers/agendamentos.py
------------------------
Define as rotas protegidas para criação e listagem de agendamentos.
"""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from .. import schemas, crud, models
from ..database import SessionLocal
from ..auth import SECRET_KEY, ALGORITHM
from jose import jwt, JWTError
from fastapi.security import OAuth2PasswordBearer

router = APIRouter(prefix="/agendamentos", tags=["Agendamentos"])

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="usuarios/login")

# Dependência para obter DB
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Decodifica o token e retorna o ID do usuário autenticado
def get_current_user_id(token: str = Depends(oauth2_scheme)) -> int:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email = payload.get("sub")
        if not email:
            raise HTTPException(status_code=401, detail="Token inválido")
    except JWTError:
        raise HTTPException(status_code=401, detail="Token inválido")

    from ..models import User
    db = SessionLocal()
    user = db.query(User).filter_by(email=email).first()
    if not user:
        raise HTTPException(status_code=401, detail="Usuário não encontrado")
    return user.id

@router.post("/", response_model=schemas.AgendamentoOut)
def criar(agendamento: schemas.AgendamentoCreate, db: Session = Depends(get_db), user_id: int = Depends(get_current_user_id)):
    try:
        return crud.criar_agendamento(db, agendamento, user_id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/", response_model=list[schemas.AgendamentoOut])
def listar(db: Session = Depends(get_db), user_id: int = Depends(get_current_user_id)):
    return crud.listar_agendamentos(db, user_id)

@router.delete("/{agendamento_id}")
def excluir(agendamento_id: int, db: Session = Depends(get_db), user_id: int = Depends(get_current_user_id)):
    sucesso = crud.deletar_agendamento(db, agendamento_id, user_id)
    if not sucesso:
        raise HTTPException(status_code=404, detail="Agendamento não encontrado")
    return {"ok": True}
