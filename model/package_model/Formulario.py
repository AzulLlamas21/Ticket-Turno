from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from model.db import Base, get_bd

class Formulario(Base):
    __tablename__ = 'formulario'
    no_turno = Column(Integer, primary_key=True)
    curp = Column(String(18), nullable=False)
    nombre = Column(String(255), nullable=False)
    paterno = Column(String(255), nullable=False)
    materno = Column(String(255), nullable=False)
    telefono = Column(String(10), nullable=False)
    celular = Column(String(10), nullable=False)
    correo = Column(String(100), nullable=False)
    id_nivel = Column(Integer, ForeignKey('nivel.id'), nullable=False)
    id_mun = Column(Integer, ForeignKey('municipio.id'), nullable=False)
    id_asunto = Column(Integer, ForeignKey('asunto.id'), nullable=False)
    estado = Column(String(255), nullable=True)

    nivel = relationship("Nivel")
    municipio = relationship("Municipio")
    asunto = relationship("Asunto")

    @staticmethod
    def obtener_formularios():
        bd = next(get_bd())
        return bd.query(Formulario).all()

    @staticmethod
    def obtener_formularios_por_municipio(id_mun):
        bd = next(get_bd())
        return bd.query(Formulario).filter_by(id_mun=id_mun).all()

    @staticmethod
    def obtener_formularios_por_nombre_municipio(municipio):
        bd = next(get_bd())
        return bd.query(Formulario).join(Formulario.municipio).filter(Municipio.nombre == municipio).all()

    @staticmethod
    def obtener_formularios_por_estado(estado):
        bd = next(get_bd())
        return bd.query(Formulario).filter_by(estado=estado).all()

    @staticmethod
    def obtener_formulario_por_no_turno(no_turno, id_mun):
        bd = next(get_bd())
        return bd.query(Formulario).filter_by(no_turno=no_turno, id_mun=id_mun).first()

    @staticmethod
    def obtener_formulario_por_nombre(nombre, paterno, materno):
        bd = next(get_bd())
        return bd.query(Formulario).filter_by(nombre=nombre, paterno=paterno, materno=materno).first()

    @staticmethod
    def obtener_formulario_por_curp(no_turno, curp):
        bd = next(get_bd())
        return bd.query(Formulario).filter_by(no_turno=no_turno, curp=curp).first()

    @staticmethod
    def agregar_formulario(obj_form):
        try:
            bd = next(get_bd())
            bd.add(obj_form)
            bd.commit()
            return 1  # Éxito
        except Exception as e:
            print(f"Error al agregar formulario: {e}")
            bd.rollback()
            return 0  # Error

    @staticmethod
    def eliminar_formulario(no_turno, id_mun):
        try:
            bd = next(get_bd())
            formulario = bd.query(Formulario).filter_by(no_turno=no_turno, id_mun=id_mun).first()
            if formulario:
                bd.delete(formulario)
                bd.commit()
                return 1  # Éxito
            else:
                return 0  # No encontrado
        except Exception as e:
            print(f"Error al eliminar formulario: {e}")
            bd.rollback()
            return 0  # Error

    @staticmethod
    def modificar_formulario(obj_form):
        try:
            bd = next(get_bd())
            formulario = bd.query(Formulario).filter_by(no_turno=obj_form.no_turno, id_mun=obj_form.id_mun).first()
            if formulario:
                formulario.curp = obj_form.curp
                formulario.nombre = obj_form.nombre
                formulario.paterno = obj_form.paterno
                formulario.materno = obj_form.materno
                formulario.telefono = obj_form.telefono
                formulario.celular = obj_form.celular
                formulario.correo = obj_form.correo
                formulario.id_nivel = obj_form.id_nivel
                formulario.id_asunto = obj_form.id_asunto
                formulario.estado = obj_form.estado
                bd.commit()
                return 1  # Éxito
            else:
                return 0  # No encontrado
        except Exception as e:
            print(f"Error al modificar formulario: {e}")
            bd.rollback()
            return 0  # Error

    @staticmethod
    def existe_formulario(curp):
        try:
            bd = next(get_bd())
            count = bd.query(Formulario).filter_by(curp=curp).count()
            return count
        except Exception as e:
            print(f"Error al verificar existencia de formulario: {e}")
            return 0

    @staticmethod
    def generar_nombre_completo(nombre, paterno, materno):
        if not materno:
            return f"{nombre} {paterno}"
        materno_completo = materno.strip().lower()
        if materno_completo in ['x', 'none', '']:
            return f"{nombre} {paterno}"
        return f"{nombre} {paterno} {materno}"