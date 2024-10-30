from models.usuario import Usuario
from sqlalchemy.orm import Session

class UsuarioRepository:
    def __init__(self, session: Session):
        self.session = session

    def salvar_usuario(self, usuario: Usuario):
        self.session.add(usuario)
        self.session.commit()
        self.session.refresh()

    def pesquisar_usuario_por_email(self, usuario: Usuario):
        return self.session.query(Usuario).filter_by(email = email).first()


    def excluir_usuario(self, usuario: Usuario):
        self.session.delete(usuario)
        self.session.commit()
        self.session.refresh(usuario)
    
        