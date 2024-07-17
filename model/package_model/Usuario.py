from model.db import db

class Usuarios(db.Model):
    no_usuario = db.Column(db.Integer, primary_key=True)
    usuario = db.Column(db.String(255), nullable=False)
    contrasena = db.Column(db.String(255), nullable=False)

    @staticmethod
    def obtener_usuarios():
        return Usuarios.query.all()

    @staticmethod
    def obtener_usuario_por_no_usuario(no_usuario):
        return Usuarios.query.filter_by(no_usuario=no_usuario).first()

    @staticmethod
    def agregar_usuario(obj_usu):
        try:
            nuevo_usuario = Usuarios(usuario=obj_usu.__usuario, contrasena=obj_usu.__contrasena)
            db.session.add(nuevo_usuario)
            db.session.commit()
            return 1  # Éxito
        except Exception as e:
            print(f"Error al agregar usuario: {e}")
            db.session.rollback()
            return 0  # Error

    @staticmethod
    def eliminar_usuario(no_usuario):
        try:
            usuario = Usuarios.query.get(no_usuario)
            if usuario:
                db.session.delete(usuario)
                db.session.commit()
                return 1  # Éxito
            else:
                return 0  # No encontrado
        except Exception as e:
            print(f"Error al eliminar usuario: {e}")
            db.session.rollback()
            return 0  # Error

    @staticmethod
    def modificar_usuario(obj_usu):
        try:
            usuario = Usuarios.query.get(obj_usu.__no_usuario)
            if usuario:
                usuario.usuario = obj_usu.__usuario
                usuario.contrasena = obj_usu.__contrasena
                db.session.commit()
                return 1  # Éxito
            else:
                return 0  # No encontrado
        except Exception as e:
            print(f"Error al modificar usuario: {e}")
            db.session.rollback()
            return 0  # Error

    @staticmethod
    def existe_usuario(usu):
        try:
            count = Usuarios.query.filter_by(usuario=usu).count()
            return count
        except Exception as e:
            print(f"Error al verificar existencia de usuario: {e}")
            return 0

    @staticmethod
    def verificar_credenciales(usu, con):
        try:
            usuario_encontrado = Usuarios.query.filter_by(usuario=usu, contrasena=con).first()
            return usuario_encontrado
        except Exception as e:
            print(f"Error al verificar credenciales: {e}")
            return None
