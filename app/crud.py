"""
crud.py
--------
Contém a lógica de acesso ao banco de dados para criação e autenticação de usuários.
-----------------------
Funções de criação, listagem, edição e exclusão de agendamentos com validação de conflito.
"""

from sqlalchemy.orm import Session
from sqlalchemy import and_
from . import models, schemas

def criar_usuario(db: Session, usuario: schemas.UserCreate):
    """
    Cria um novo usuário no banco, se o e-mail ainda não existir.
    """
    usuario_existente = db.query(models.User).filter_by(email=usuario.email).first()
    if usuario_existente:
        raise ValueError("Email já cadastrado")

    usuario_db = models.User(
        nome=usuario.nome,
        email=usuario.email,
        senha_hash=auth.criar_hash(usuario.senha)
    )
    db.add(usuario_db)
    db.commit()
    db.refresh(usuario_db)
    return usuario_db

def autenticar_usuario(db: Session, email: str, senha: str):
    """
    Verifica se o e-mail e senha estão corretos. Retorna o usuário ou None.
    """
    usuario = db.query(models.User).filter_by(email=email).first()
    if not usuario or not auth.verificar_senha(senha, usuario.senha_hash):
        return None
    return usuario

def criar_agendamento(db: Session, agendamento: schemas.AgendamentoCreate, usuario_id: int):
    # Verifica conflito de horário para o mesmo usuário
    conflito = db.query(models.Agendamento).filter(
        and_(
            models.Agendamento.usuario_id == usuario_id,
            models.Agendamento.data_hora == agendamento.data_hora
        )
    ).first()

    if conflito:
        raise ValueError("Já existe um agendamento neste horário.")

    novo = models.Agendamento(
        data_hora=agendamento.data_hora,
        local=agendamento.local,
        descricao=agendamento.descricao,
        usuario_id=usuario_id
    )
    db.add(novo)
    db.commit()
    db.refresh(novo)
    return novo

def listar_agendamentos(db: Session, usuario_id: int):
    return db.query(models.Agendamento).filter_by(usuario_id=usuario_id).all()

def deletar_agendamento(db: Session, agendamento_id: int, usuario_id: int):
    ag = db.query(models.Agendamento).filter_by(id=agendamento_id, usuario_id=usuario_id).first()
    if not ag:
        return False
    db.delete(ag)
    db.commit()
    return True