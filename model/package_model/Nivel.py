from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from model.db import Base, get_bd

class Nivel(Base):
    __tablename__ = 'nivel'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nivel = Column(String(2), nullable=False)

    @staticmethod
    def obtener_niveles():
        bd = next(get_bd())
        return [(nivel.id, nivel.nivel) for nivel in bd.query(Nivel).all()]

    @staticmethod
    def obtener_nivel_por_id(id):
        bd = next(get_bd())
        return bd.query(Nivel).filter_by(id=id).first()

    @staticmethod
    def obtener_nombre_por_id(id):
        try:
            bd = next(get_bd())
            nivel = bd.query(Nivel).filter(Nivel.id == id).first()
            return nivel.nivel if nivel else None
        except Exception as e:
            print(f"Error al obtener nombre de asunto por ID: {e}")
            return None
    
    @staticmethod
    def agregar_nivel(obj_nv):
        try:
            bd = next(get_bd())
            nuevo_nivel = Nivel(nivel=obj_nv.nivel)
            bd.add(nuevo_nivel)
            bd.commit()
            return 1  # Éxito
        except Exception as e:
            print(f"Error al agregar nivel: {e}")
            bd.rollback()
            return 0  # Error

    @staticmethod
    def eliminar_nivel(id):
        try:
            bd = next(get_bd())
            nivel = bd.query(Nivel).get(id)
            if nivel:
                bd.delete(nivel)
                bd.commit()
                return 1  # Éxito
            else:
                return 0  # No encontrado
        except Exception as e:
            print(f"Error al eliminar nivel: {e}")
            bd.rollback()
            return 0  # Error

    @staticmethod
    def modificar_nivel(obj_nv):
        try:
            bd = next(get_bd())
            nivel = bd.query(Nivel).get(obj_nv.id)
            if nivel:
                nivel.nivel = obj_nv.nivel
                bd.commit()
                return 1  # Éxito
            else:
                return 0  # No encontrado
        except Exception as e:
            print(f"Error al modificar nivel: {e}")
            bd.rollback()
            return 0  # Error

    @staticmethod
    def existe_nivel(nv):
        try:
            bd = next(get_bd())
            count = bd.query(Nivel).filter_by(nivel=nv).count()
            return count
        except Exception as e:
            print(f"Error al verificar existencia de nivel: {e}")
            return 0
