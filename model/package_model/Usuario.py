from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from model.db import Base, get_bd

class Usuario(Base):
    __tablename__ = 'usuarios'
    no_usuario = Column(Integer, primary_key=True, autoincrement=True)
    usuario = Column(String(30), nullable=False)
    contrasena = Column(String(20), nullable=False)

    @staticmethod
    def obtener_usuarios():
        bd = next(get_bd())
        return bd.query(Usuario).all()

    @staticmethod
    def obtener_usuario_por_no_usuario(no_usuario):
        bd = next(get_bd())
        return bd.query(Usuario).filter_by(no_usuario=no_usuario).first()

    @staticmethod
    def agregar_usuario(obj_usu):
        try:
            bd = next(get_bd())
            nuevo_usuario = Usuario(usuario=obj_usu.usuario, contrasena=obj_usu.contrasena)
            bd.add(nuevo_usuario)
            bd.commit()
            return 1  # Éxito
        except Exception as e:
            print(f"Error al agregar usuario: {e}")
            bd.rollback()
            return 0  # Error

    @staticmethod
    def eliminar_usuario(no_usuario):
        try:
            bd = next(get_bd())
            usuario = bd.query(Usuario).get(no_usuario)
            if usuario:
                bd.delete(usuario)
                bd.commit()
                return 1  # Éxito
            else:
                return 0  # No encontrado
        except Exception as e:
            print(f"Error al eliminar usuario: {e}")
            bd.rollback()
            return 0  # Error

    @staticmethod
    def modificar_usuario(obj_usu):
        try:
            bd = next(get_bd())
            usuario = bd.query(Usuario).get(obj_usu.no_usuario)
            if usuario:
                usuario.usuario = obj_usu.usuario
                usuario.contrasena = obj_usu.contrasena
                bd.commit()
                return 1  # Éxito
            else:
                return 0  # No encontrado
        except Exception as e:
            print(f"Error al modificar usuario: {e}")
            bd.rollback()
            return 0  # Error

    @staticmethod
    def existe_usuario(usu):
        try:
            bd = next(get_bd())
            count = bd.query(Usuario).filter_by(usuario=usu).count()
            return count
        except Exception as e:
            print(f"Error al verificar existencia de usuario: {e}")
            return 0

    @staticmethod
    def verificar_credenciales(usu, con):
        try:
            bd = next(get_bd())
            usuario_encontrado = bd.query(Usuario).filter_by(usuario=usu, contrasena=con).first()
            return usuario_encontrado
        except Exception as e:
            print(f"Error al verificar credenciales: {e}")
            return None
