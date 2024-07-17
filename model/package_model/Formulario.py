from model.db import db

class Formulario(db.Model):
    no_turno = db.Column(db.Integer, primary_key=True)
    curp = db.Column(db.String(18), nullable=False)
    nombre = db.Column(db.String(255), nullable=False)
    paterno = db.Column(db.String(255), nullable=False)
    materno = db.Column(db.String(255))
    telefono = db.Column(db.String(10))
    celular = db.Column(db.String(10))
    correo = db.Column(db.String(100))
    id_nivel = db.Column(db.Integer, nullable=False)
    id_mun = db.Column(db.Integer, nullable=False)
    id_asunto = db.Column(db.Integer, nullable=False)
    estado = db.Column(db.String(255))

    @staticmethod
    def obtener_formularios():
        return Formulario.query.all()

    @staticmethod
    def obtener_formularios_por_municipio(id_mun):
        return Formulario.query.filter_by(id_mun=id_mun).all()

    @staticmethod
    def obtener_formularios_por_nombre_municipio(municipio):
        return Formulario.query.filter_by(municipio=municipio).all()

    @staticmethod
    def obtener_formularios_por_estado(estado):
        return Formulario.query.filter_by(estado=estado).all()

    @staticmethod
    def obtener_formulario_por_no_turno(no_turno, id_mun):
        return Formulario.query.filter_by(no_turno=no_turno, id_mun=id_mun).first()

    @staticmethod
    def obtener_formulario_por_nombre(nombre, paterno, materno):
        return Formulario.query.filter_by(nombre=nombre, paterno=paterno, materno=materno).first()

    @staticmethod
    def obtener_formulario_por_curp(no_turno, curp):
        return Formulario.query.filter_by(no_turno=no_turno, curp=curp).first()

    @staticmethod
    def agregar_formulario(obj_form):
        try:
            nuevo_formulario = Formulario(
                no_turno=obj_form.__no_turno,
                curp=obj_form.__curp,
                nombre=obj_form.__nombre,
                paterno=obj_form.__paterno,
                materno=obj_form.__materno,
                telefono=obj_form.__telefono,
                celular=obj_form.__celular,
                correo=obj_form.__correo,
                id_nivel=obj_form.__id_nivel,
                id_mun=obj_form.__id_mun,
                id_asunto=obj_form.__id_asunto,
                estado=obj_form.__estado
            )
            db.session.add(nuevo_formulario)
            db.session.commit()
            return 1  # Éxito
        except Exception as e:
            print(f"Error al agregar formulario: {e}")
            db.session.rollback()
            return 0  # Error

    @staticmethod
    def eliminar_formulario(no_turno, id_mun):
        try:
            formulario = Formulario.query.filter_by(no_turno=no_turno, id_mun=id_mun).first()
            if formulario:
                db.session.delete(formulario)
                db.session.commit()
                return 1  # Éxito
            else:
                return 0  # No encontrado
        except Exception as e:
            print(f"Error al eliminar formulario: {e}")
            db.session.rollback()
            return 0  # Error

    @staticmethod
    def modificar_formulario(obj_form):
        try:
            formulario = Formulario.query.filter_by(no_turno=obj_form.__no_turno, id_mun=obj_form.__id_mun).first()
            if formulario:
                formulario.curp = obj_form.__curp
                formulario.nombre = obj_form.__nombre
                formulario.paterno = obj_form.__paterno
                formulario.materno = obj_form.__materno
                formulario.telefono = obj_form.__telefono
                formulario.celular = obj_form.__celular
                formulario.correo = obj_form.__correo
                formulario.id_nivel = obj_form.__id_nivel
                formulario.id_asunto = obj_form.__id_asunto
                formulario.estado = obj_form.__estado
                db.session.commit()
                return 1  # Éxito
            else:
                return 0  # No encontrado
        except Exception as e:
            print(f"Error al modificar formulario: {e}")
            db.session.rollback()
            return 0  # Error

    @staticmethod
    def existe_formulario(curp):
        try:
            count = Formulario.query.filter_by(curp=curp).count()
            return count
        except Exception as e:
            print(f"Error al verificar existencia de formulario: {e}")
            return 0

    @staticmethod
    def generar_nombre_completo(nombre, paterno, materno):
        if materno is None:
            materno = ''
        materno_completo = materno.strip().lower()
        if materno_completo == 'x':
            return f"{nombre} {paterno}"
        elif materno_completo == '' or materno_completo == 'none':
            return f"{nombre} {paterno}"
        else:
            return f"{nombre} {paterno} {materno}"
