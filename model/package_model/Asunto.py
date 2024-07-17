from model.db import db

class Asunto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    asunto = db.Column(db.String(50), nullable=False)

    @staticmethod
    def obtener_asuntos():
        return Asunto.query.all()

    @staticmethod
    def obtener_asunto_por_id(id):
        return Asunto.query.filter_by(id=id).first()

    @staticmethod
    def agregar_asunto(obj_asto):
        try:
            nuevo_asunto = Asunto(asunto=obj_asto.__nombre_asunto)
            db.session.add(nuevo_asunto)
            db.session.commit()
            return 1  # Éxito
        except Exception as e:
            print(f"Error al agregar asunto: {e}")
            db.session.rollback()
            return 0  # Error

    @staticmethod
    def eliminar_asunto(id):
        try:
            asunto = Asunto.query.get(id)
            if asunto:
                db.session.delete(asunto)
                db.session.commit()
                return 1  # Éxito
            else:
                return 0  # No encontrado
        except Exception as e:
            print(f"Error al eliminar asunto: {e}")
            db.session.rollback()
            return 0  # Error

    @staticmethod
    def modificar_asunto(obj_asto):
        try:
            asunto = Asunto.query.get(obj_asto.__id_asunto)
            if asunto:
                asunto.asunto = obj_asto.__nombre_asunto
                db.session.commit()
                return 1  # Éxito
            else:
                return 0  # No encontrado
        except Exception as e:
            print(f"Error al modificar asunto: {e}")
            db.session.rollback()
            return 0  # Error

    @staticmethod
    def existe_asunto(asto):
        try:
            count = Asunto.query.filter_by(asunto=asto).count()
            return count
        except Exception as e:
            print(f"Error al verificar existencia de asunto: {e}")
            return 0
