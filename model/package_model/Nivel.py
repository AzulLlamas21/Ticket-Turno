from model.db import db

class Nivel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nivel = db.Column(db.String(255), nullable=False)

    @staticmethod
    def obtener_niveles():
        return Nivel.query.all()

    @staticmethod
    def obtener_nivel_por_id(id):
        return Nivel.query.filter_by(id=id).first()

    @staticmethod
    def agregar_nivel(obj_nv):
        try:
            nuevo_nivel = Nivel(nivel=obj_nv.__nombre_nivel)
            db.session.add(nuevo_nivel)
            db.session.commit()
            return 1  # Éxito
        except Exception as e:
            print(f"Error al agregar nivel: {e}")
            db.session.rollback()
            return 0  # Error

    @staticmethod
    def eliminar_nivel(id):
        try:
            nivel = Nivel.query.get(id)
            if nivel:
                db.session.delete(nivel)
                db.session.commit()
                return 1  # Éxito
            else:
                return 0  # No encontrado
        except Exception as e:
            print(f"Error al eliminar nivel: {e}")
            db.session.rollback()
            return 0  # Error

    @staticmethod
    def modificar_nivel(obj_nv):
        try:
            nivel = Nivel.query.get(obj_nv.__id_nivel)
            if nivel:
                nivel.nivel = obj_nv.__nombre_nivel
                db.session.commit()
                return 1  # Éxito
            else:
                return 0  # No encontrado
        except Exception as e:
            print(f"Error al modificar nivel: {e}")
            db.session.rollback()
            return 0  # Error

    @staticmethod
    def existe_nivel(nv):
        try:
            count = Nivel.query.filter_by(nivel=nv).count()
            return count
        except Exception as e:
            print(f"Error al verificar existencia de nivel: {e}")
            return 0
