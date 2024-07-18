from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from model.db import Base, get_bd

class Municipio(Base):
    __tablename__ = 'municipio'
    id = Column(Integer, primary_key=True, autoincrement=True)
    municipio = Column(String(255), nullable=False)
    
    formularios = relationship("Formulario", back_populates="municipio")

    @staticmethod
    def obtener_municipios():
        bd = next(get_bd())
        return [(municipio.id, municipio.municipio) for municipio in bd.query(Municipio).all()]

    @staticmethod
    def obtener_todos_los_municipios():
        bd = next(get_bd())
        return bd.query(Municipio).all()
    
    @staticmethod
    def obtener_municipio_por_id(id):
        bd = next(get_bd())
        return bd.query(Municipio).filter_by(id=id).first()

    @staticmethod
    def obtener_nombre_por_id(id):
        try:
            bd = next(get_bd())
            municipio = bd.query(Municipio).filter(Municipio.id == id).first()
            return municipio.municipio if municipio else None
        except Exception as e:
            print(f"Error al obtener nombre de asunto por ID: {e}")
            return None
    
    @staticmethod
    def agregar_municipio(obj_mun):
        try:
            bd = next(get_bd())
            nuevo_municipio = Municipio(municipio=obj_mun.municipio)
            bd.add(nuevo_municipio)
            bd.commit()
            return 1  # Éxito
        except Exception as e:
            print(f"Error al agregar municipio: {e}")
            bd.rollback()
            return 0  # Error

    @staticmethod
    def eliminar_municipio(id):
        try:
            bd = next(get_bd())
            municipio = bd.query(Municipio).get(id)
            if municipio:
                bd.delete(municipio)
                bd.commit()
                return 1  # Éxito
            else:
                return 0  # No encontrado
        except Exception as e:
            print(f"Error al eliminar municipio: {e}")
            bd.rollback()
            return 0  # Error

    @staticmethod
    def modificar_municipio(obj_mun):
        try:
            bd = next(get_bd())
            municipio = bd.query(Municipio).get(obj_mun.id)
            if municipio:
                municipio.municipio = obj_mun.municipio
                bd.commit()
                return 1  # Éxito
            else:
                return 0  # No encontrado
        except Exception as e:
            print(f"Error al modificar municipio: {e}")
            bd.rollback()
            return 0  # Error

    @staticmethod
    def existe_municipio(mun):
        try:
            bd = next(get_bd())
            count = bd.query(Municipio).filter_by(municipio=mun).count()
            return count
        except Exception as e:
            print(f"Error al verificar existencia de municipio: {e}")
            return 0