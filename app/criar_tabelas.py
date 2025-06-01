# app/criar_tabelas.py

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from .database import Base, engine
from . import models

def criar_tabelas():
    print("Criando tabelas no banco de dados...")
    Base.metadata.create_all(bind=engine)
    print("Tabelas criadas com sucesso.")

if __name__ == "__main__":
    criar_tabelas()
