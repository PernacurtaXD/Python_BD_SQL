from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import declarative_base as Base
from config.database import db

class Usuario(Base):

    id = Column(Integer, primary_key= True, autoincrement= True)
    nome = Column(String(150))
    email = Column(String(150))
    senha = Column(String(150))


    def __init__(self,nome: str, email: str, senha: str):
        self.nome = nome
        self.nome = nome
        self.nome = nome

Base.metadata.create_all(bind=db)