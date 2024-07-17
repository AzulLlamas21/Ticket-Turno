from model.db import db

class Municipio(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    municipio = db.Column(db.String(255), nullable=False)

    @staticmethod
    def obtener_municipios():
        return Municipio.query.all()

    @staticmethod
    def obtener_municipio_por_id(id):
        return Municipio.query.filter_by(id=id).first()

    @staticmethod
    def agregar_municipio(obj_mun):
        try:
            nuevo_municipio = Municipio(municipio=obj_mun.__nombre_municipio)
            db.session.add(nuevo_municipio)
            db.session.commit()
            return 1  # Éxito
        except Exception as e:
            print(f"Error al agregar municipio: {e}")
            db.session.rollback()
            return 0  # Error

    @staticmethod
    def eliminar_municipio(id):
        try:
            municipio = Municipio.query.get(id)
            if municipio:
                db.session.delete(municipio)
                db.session.commit()
                return 1  # Éxito
            else:
                return 0  # No encontrado
        except Exception as e:
            print(f"Error al eliminar municipio: {e}")
            db.session.rollback()
            return 0  # Error

    @staticmethod
    def modificar_municipio(obj_mun):
        try:
            municipio = Municipio.query.get(obj_mun.__id_municipio)
            if municipio:
                municipio.municipio = obj_mun.__nombre_municipio
                db.session.commit()
                return 1  # Éxito
            else:
                return 0  # No encontrado
        except Exception as e:
            print(f"Error al modificar municipio: {e}")
            db.session.rollback()
            return 0  # Error

    @staticmethod
    def existe_municipio(mun):
        try:
            count = Municipio.query.filter_by(municipio=mun).count()
            return count
        except Exception as e:
            print(f"Error al verificar existencia de municipio: {e}")
            return 0
