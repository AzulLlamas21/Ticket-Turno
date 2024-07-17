from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from model.db import Base, get_bd

class Asunto(Base):
    __tablename__ = 'asunto'
    id = Column(Integer, primary_key=True, autoincrement=True)
    asunto = Column(String(50), nullable=False)

    @staticmethod
    def obtener_asuntos():
        bd = next(get_bd())
        return [(asunto.id, asunto.asunto) for asunto in bd.query(Asunto).all()]

    @staticmethod
    def obtener_asunto_por_id(id):
        bd = next(get_bd())
        return bd.query(Asunto).filter(Asunto.id == id).first()
    
    @staticmethod
    def obtener_nombre_por_id(id):
        try:
            bd = next(get_bd())
            asunto = bd.query(Asunto).filter(Asunto.id == id).first()
            return asunto.asunto if asunto else None
        except Exception as e:
            print(f"Error al obtener nombre de asunto por ID: {e}")
            return None

    @staticmethod
    def agregar_asunto(obj_asto):
        try:
            bd = next(get_bd())
            último_id = bd.query(Asunto).order_by(Asunto.id.desc()).first().id
            obj_asto.id = (último_id+1)
            bd.add(obj_asto)
            bd.commit()
            return 1  # Éxito
        except Exception as e:
            print(f"Error al agregar asunto: {e}")
            return 0  # Error

    @staticmethod
    def eliminar_asunto(id):
        try:
            bd = next(get_bd())
            asunto = bd.query(Asunto).filter(Asunto.id == id).first()
            if asunto:
                bd.delete(asunto)
                bd.commit()
                return 1  # Éxito
            else:
                return 0  # No encontrado
        except Exception as e:
            print(f"Error al eliminar asunto: {e}")
            return 0  # Error

    @staticmethod
    def modificar_asunto(obj_asto):
        try:
            bd = next(get_bd())
            asunto = bd.query(Asunto).filter(Asunto.id == obj_asto.id).first()
            if asunto:
                asunto.asunto = obj_asto.asunto
                bd.commit()
                return 1  # Éxito
            else:
                return 0  # No encontrado
        except Exception as e:
            print(f"Error al modificar asunto: {e}")
            return 0  # Error

    @staticmethod
    def existe_asunto(asto):
        try:
            bd = next(get_bd())
            count = bd.query(Asunto).filter(Asunto.asunto==asto).count()
            return count
        except Exception as e:
            print(f"Error al verificar existencia de asunto: {e}")
            return 0