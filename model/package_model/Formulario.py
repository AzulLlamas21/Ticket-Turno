import model.package_model.Database as Database

class Formulario:
    def __init__(self, no_turno=0, curp='', nombre='', paterno='', materno='', telefono='', celular='', correo='', id_nivel=0, id_mun=0, id_asunto=0, estado=''):
        self.__no_turno = no_turno
        self.__curp = curp
        self.__nombre = nombre
        self.__paterno = paterno
        self.__materno = materno
        self.__telefono = telefono
        self.__celular = celular
        self.__correo = correo
        self.__id_nivel = id_nivel
        self.__id_mun = id_mun
        self.__id_asunto = id_asunto
        self.__estado = estado

    def obtener_formularios(self):
        conexion = Database.Database()
        formularios = []
        with conexion.cursor as cursor:
            cursor.execute("SELECT * FROM formulario")
            formularios = cursor.fetchall()
        conexion.conn.close()
        return formularios

    def obtener_formulario_por_no_turno(self, no_turno, id_mun):
        conexion = Database.Database()
        formulario = None
        with conexion.cursor as cursor:
            cursor.execute("SELECT * FROM formulario WHERE no_turno = %s and id_mun = %s", (no_turno, id_mun))
            formulario = cursor.fetchone()
        conexion.conn.close()
        return formulario
    
    def obtener_formulario_por_nombre(self, nombre, paterno, materno):
        conexion = Database.Database()
        formulario = None
        with conexion.cursor as cursor:
            cursor.execute("SELECT * FROM formulario WHERE nombre = %s and paterno = %s and materno = %s", (nombre, paterno, materno))
            formulario = cursor.fetchone()
        conexion.conn.close()
        return formulario
    
    def obtener_formulario_por_curp(self, curp):
        conexion = Database.Database()
        formulario = None
        with conexion.cursor as cursor:
            cursor.execute("SELECT * FROM formulario WHERE curp = %s", (curp))
            formulario = cursor.fetchone()
        conexion.conn.close()
        return formulario

    def agregar_formulario(self, obj_form):
        conexion = Database.Database()
        with conexion.cursor as cursor:
            try:
                cursor.execute("SELECT no_turno FROM formulario WHERE id_mun = %s ORDER BY no_turno DESC LIMIT 1", (obj_form.__id_mun))
                result = cursor.fetchone()
                no_turno = 1
                if result is not None:
                    no_turno = result[0] + 1
                sql = """INSERT INTO formulario(no_turno, curp, nombre, paterno, materno, telefono, celular, correo, id_nivel, id_mun, id_asunto, estado)
                         VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
                
                vals = (no_turno, obj_form.__curp, obj_form.__nombre, obj_form.__paterno, obj_form.__materno, obj_form.__telefono, obj_form.__celular, obj_form.__correo, obj_form.__id_nivel, obj_form.__id_mun, obj_form.__id_asunto, obj_form.__estado)
                print(vals)
                affected = cursor.execute(sql, vals)
                conexion.conn.commit()
                return affected
            except pymysql.err.ProgrammingError as except_detail:
                print(f"pymysql.err.ProgrammingError: {except_detail}")
                return 0
            except Exception as e:
                print(f"Exception: {e}")
                return 0
            finally:
                conexion.conn.close()

    def eliminar_formulario(self, no_turno, id_mun):
        conexion = Database.Database()
        affected = 0
        with conexion.cursor as cursor:
            try:
                sql = "DELETE FROM formulario WHERE no_turno = %s and id_mun = %s"
                vals = (no_turno, id_mun)
                affected = cursor.execute(sql, vals)
                conexion.conn.commit()
                return affected
            except pymysql.err.ProgrammingError as except_detail:
                print(f"pymysql.err.ProgrammingError: {except_detail}")
                return 0
            except Exception as e:
                print(f"Exception: {e}")
                return 0
            finally:
                conexion.conn.close()

    def modificar_formulario(self, obj_form):
        conexion = Database.Database()
        with conexion.cursor as cursor:
            try:
                sql = """UPDATE formulario SET curp = %s, nombre = %s, paterno = %s, materno = %s, telefono = %s, 
                        celular = %s, correo = %s, id_nivel = %s, id_asunto = %s, estado = %s 
                        WHERE no_turno = %s and id_mun = %s"""
                vals = (obj_form.__curp, obj_form.__nombre, obj_form.__paterno, obj_form.__materno, obj_form.__telefono, obj_form.__celular, obj_form.__correo, obj_form.__id_nivel, obj_form.__id_asunto, obj_form.__estado, obj_form.__no_turno, obj_form.__id_mun)
                affected = cursor.execute(sql, vals)
                conexion.conn.commit()
                return affected
            except pymysql.err.ProgrammingError as except_detail:
                return print("pymysql.err.ProgrammingError: {0}".format(except_detail))
            except Exception as e:
                return e
            finally:
                conexion.conn.close()

    @staticmethod
    def existe_formulario(curp):
        conexion = Database.Database()
        formulario = None
        with conexion.cursor as cursor:
            sql = "SELECT count(*) as ex FROM formulario WHERE curp = %s"
            vals = (curp)
            cursor.execute(sql, vals)
            formulario = cursor.fetchone()
        conexion.conn.close()
        return formulario[0]
