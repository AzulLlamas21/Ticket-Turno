from flask import Flask, render_template, url_for, request, redirect, jsonify, send_file, session
from model.db import init_db
from model.package_model.Usuario import Usuario
from model.package_model.Formulario import Formulario
from model.package_model.Nivel import Nivel
from model.package_model.Municipio import Municipio
from model.package_model.Asunto import Asunto
import os
import qrcode
import matplotlib.pyplot as plt
import io
import base64
import pandas as pd
from fpdf import FPDF
#from sqlalchemy import SQLAlchemy


app = Flask(__name__)
init_db
app.secret_key = 'keykey'
HCAPTCHA_SECRET = 'ES_ef2fbcaf50b4434f9d9b9d05d4cd6ae3'


# Función para verificar y obtener el nombre del archivo existente
def obtener_archivo_existente(dir_path, filename_pattern):
    files = os.listdir(dir_path)
    for file in files:
        if file.startswith(filename_pattern):
            return file
    return None

#INDEX
@app.route('/')
def index():
    lista_niveles = Nivel.obtener_niveles()
    lista_municipios = Municipio.obtener_municipios()
    lista_asuntos = Asunto.obtener_asuntos()
    return render_template('Index.html', lista_niveles=lista_niveles, lista_municipios=lista_municipios, lista_asuntos=lista_asuntos)

#LOGIN
@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'admin' in session:
        return redirect(url_for('admin'))
    if request.method == 'POST':
        usuario = request.get_json()['f_user']
        contrasena = request.get_json()['f_pwd']
        
        usuario_model = Usuario()
        user = usuario_model.verificar_credenciales(usuario, contrasena)

        if user:
            session['admin'] = {'user': usuario, 'pass': contrasena}
            return jsonify({'redirect': url_for('admin')})
        else:
            return jsonify({'message': 'Usuario o contraseña incorrectos'})

    return render_template('login.html')

#CERRAR Y REGRESAR A INDEX
@app.route('/logout')
def logout():
    session.pop('admin', None)
    return redirect(url_for('index'))

#CERRAR Y REGRESAR A LOGIN
@app.route('/admin_logout')
def admin_logout():
    session.pop('admin', None)
    return redirect(url_for('login'))

#ADMINISTRADOR(OBTENER LISTA DE FORMULARIO)
@app.route('/admin')
def admin():
    if 'admin' not in session:
        return redirect(url_for('login'))
    query = request.args.get('query')
    forms = []
    if not query:
        forms = Formulario.obtener_formularios()
    else:
        forms = Formulario.obtener_formularios_query(query)
    return render_template('admin.html', forms=forms)

#IR A ACTUALIZAR
@app.route('/actualizar')
def actualizar():
    if 'admin' not in session:
        return redirect(url_for('login'))
    
    lista_niveles = Nivel.obtener_niveles()
    lista_municipios = Municipio.obtener_municipios()
    lista_asuntos = Asunto.obtener_asuntos()
    
    # Verificar y manejar caso de listas vacías aquí si es necesario
    
    return render_template('actualizar.html', lista_niveles=lista_niveles, lista_municipios=lista_municipios, lista_asuntos=lista_asuntos)

#IR A ACTUALIZAR FORMULARIO CON DATOS EXISTENTES
@app.route('/update/<int:no_turno>/<int:id_mun>')
def update(no_turno, id_mun):
    if 'admin' not in session:
        return redirect(url_for('login'))
    formulario = Formulario.obtener_formulario_por_no_turno(no_turno, id_mun)
    if not formulario:
        return redirect(url_for('admin'))
    return render_template('actualizar.html', formulario=formulario)

#IR A DASHBOARD
@app.route('/dashboard')
def dashboard():
    if not 'admin' in session:
        return redirect(url_for('login'))
    return render_template('dashboard.html')

# DASHBOARD: Gráfico Circular de Total de Solicitudes
@app.route('/dashboard/circular')
def dashboard_circular():
    try:
        formulario_model = Formulario()
        forms = formulario_model.obtener_formularios()

        df = pd.DataFrame([form.__dict__ for form in forms])
        estado_counts = df['estado'].value_counts()

        plt.figure(figsize=(10, 6))
        estado_counts.plot(kind='pie', autopct=lambda p: '{:.1f}% ({:.0f})'.format(p, (p/100)*estado_counts.sum()), colors=['green', 'blue', 'red'])
        plt.title('Estado de Solicitudes')

        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)
        image_base64 = base64.b64encode(buf.getvalue()).decode('utf-8')
        buf.close()

        return jsonify({'image': 'data:image/png;base64,{}'.format(image_base64)})
    except Exception as e:
        print(f"Error en /dashboard/circular: {e}")
        return jsonify({'error': str(e)}), 500

# DASHBOARD: Gráfico de Barras de Solicitudes por Municipio
@app.route('/dashboard/bar')
def dashboard_bar():
    try:
        municipio = request.args.get('municipio', '')
        print(f"Municipio recibido: {municipio}")  # Debug print
        formulario_model = Formulario()

        if municipio:
            forms = formulario_model.obtener_formularios_por_nombre_municipio(municipio)
        else:
            forms = formulario_model.obtener_formularios()

        df = pd.DataFrame([form.__dict__ for form in forms])
        print(f"DataFrame creado con {len(df)} formularios")  # Debug print
    
        municipios = df['id_mun'].unique()
        estados = ['Pendiente', 'Activo', 'Resuelto']

        data = {mun: {estado: 0 for estado in estados} for mun in municipios}
        for index, row in df.iterrows():
            data[row['id_mun']][row['estado']] += 1

        municipio_model = Municipio()
        municipio_names = {m[0]: m[1] for m in municipio_model.obtener_municipios()}
        print(f"Nombre de municipios obtenidos: {municipio_names}")  # Debug print

        plt.figure(figsize=(15, 8))
        bar_width = 0.25
        positions = range(len(municipios))
        for i, estado in enumerate(estados):
            plt.bar([pos + i*bar_width for pos in positions], [data[m][estado] for m in municipios], bar_width, align='center', label=estado)

        plt.xticks([pos + bar_width for pos in positions], [municipio_names[m] for m in municipios])
        plt.title('Estado de Solicitudes por Municipio')
        plt.xlabel('Municipio')
        plt.ylabel('Cantidad')
        plt.legend()

        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)
        image_base64 = base64.b64encode(buf.getvalue()).decode('utf-8')
        buf.close()

        return jsonify({'image': 'data:image/png;base64,{}'.format(image_base64)})
    except Exception as error:
        print(f"Error en /dashboard/bar: {error}")  # Debug print
        return jsonify({'error': str(error)}), 500

#BUSCAR FORMULARIO
@app.route('/buscar_formulario', methods=['GET'])
def buscar_formulario():
    no_turno = request.args.get('no_turno')
    curp = request.args.get('curp')

    # Realiza la búsqueda en la base de datos y devuelve el formulario correspondiente
    formulario = Formulario.obtener_formulario_por_curp(no_turno, curp)

    if formulario:
        return jsonify(success=True, formulario=formulario.to_dict())
    return jsonify(success=False)

# @app.route('/agregar_formulario', methods=['POST'])
# def agregar_formulario():
#     data = request.get_json()
#     # Agrega el formulario a la base de datos
#     nuevo_formulario = Formulario(**data)
#     db.session.add(nuevo_formulario)
#     db.session.commit()
#     return jsonify(success=True)

#ACTUALIZA EL FORMULARIO EN LA BD
@app.route('/actualizar_formulario', methods=['POST'])
def actualizar_formulario():
    data = request.get_json()
    # Actualiza el formulario en la base de datos
    formulario = Formulario.obtener_formulario_por_no_turno(data['no_turno'], data['id_mun'])
    if formulario:
        for key, value in data.items():
            setattr(formulario, key, value)
        Formulario.modificar_formulario(formulario)
        return jsonify(success=True)
    return jsonify(success=False)

#ELIMINA EL FORMULARIO
@app.route('/delete/<int:no_turno>/<int:id_mun>', methods=['POST'])
def delete(no_turno, id_mun):
    if 'admin' not in session:
        return redirect(url_for('login'))
    resultado = Formulario.eliminar_formulario(no_turno, id_mun)
    if resultado:
        return redirect(url_for('admin'))
    return jsonify(success=False)

#GENERAR TICKET
@app.route('/generar_ticket', methods=['POST'])
def generar_ticket():
    try:
        # Recoger los datos del formulario
        f_nc = Formulario.generar_nombre_completo(
            request.form['f_nombre'],
            request.form['f_paterno'],
            request.form['f_materno']
        )
        f_curp = request.form['f_curp']
        f_nombre = request.form['f_nombre']
        f_paterno = request.form['f_paterno']
        f_materno = request.form['f_materno']
        f_telefono = request.form['f_telefono']
        f_celular = request.form['f_celular']
        f_correo = request.form['f_correo']
        f_nivel = request.form['f_nivel']
        f_mun = request.form['f_mun']
        f_asunto = request.form['f_asunto']

        # Crear una instancia de Formulario y guardar en la base de datos
        nuevo_formulario = Formulario(
            curp=f_curp, nombre=f_nombre, paterno=f_paterno, materno=f_materno, 
            telefono=f_telefono, celular=f_celular, correo=f_correo, 
            id_nivel=f_nivel, id_mun=f_mun, id_asunto=f_asunto, estado='Pendiente'
        )

        # Guardar el formulario en la base de datos
        resultado = Formulario.agregar_formulario(nuevo_formulario)
        if resultado == 1:
            # Éxito al guardar en la base de datos
            no_turno = Formulario.obtener_no_turno_por_nombre_y_curp(f_nombre, f_paterno, f_materno, f_curp)
            datos = {
                'nombre_completo': f_nc,
                'curp': f_curp,
                'nombre': f_nombre,
                'paterno': f_paterno,
                'materno': f_materno,
                'telefono': f_telefono,
                'celular': f_celular,
                'correo': f_correo,
                'nivel': Nivel.obtener_nombre_por_id(f_nivel),
                'municipio': Municipio.obtener_nombre_por_id(f_mun),
                'asunto': Asunto.obtener_nombre_por_id(f_asunto),
                'no_turno': no_turno
            }
            return render_template('Ticket.html', datos=datos)
        else:
            # Error al guardar en la base de datos
            return redirect(url_for('index'))

    except Exception as e:
        print(f"Error al generar el ticket: {e}")
        return redirect(url_for('index'))

#IR A TICKET
@app.route('/ticket')
def ticket():
    return render_template('Ticket.html', data=request.args.to_dict())

#GENERAR PDF
@app.route('/generar_pdf', methods=['POST'])
def generar_pdf():
    try:
        # Obtener datos del formulario
        data = request.json

        # Directorios para guardar PDFs y QRs
        pdf_dir = os.path.join(app.root_path, 'static', 'pdf')
        qr_dir = os.path.join(app.root_path, 'static', 'qr')

        # Crear directorios si no existen
        if not os.path.exists(pdf_dir):
            os.makedirs(pdf_dir)
        if not os.path.exists(qr_dir):
            os.makedirs(qr_dir)

        # Generar nombre del archivo PDF y QR
        pdf_filename = f"{data['curp']}_{data['no_turno']}_ticket.pdf"
        pdf_output = os.path.join(pdf_dir, pdf_filename)

        # Verificar si ya existe un PDF con el mismo nombre
        if os.path.exists(pdf_output):
            pdf_url = url_for('static', filename=f'pdf/{pdf_filename}', _external=True)
            return jsonify({'success': True, 'pdf_url': pdf_url})

        # Contenido del QR
        qr_content = f"CURP: {data['curp']}, No Turno: {data['no_turno']}"
        qr_filename = f"{data['curp']}_{data['no_turno']}_qr.png"
        qr_output = os.path.join(qr_dir, qr_filename)

        # Verificar si ya existe un QR con el mismo nombre
        if not os.path.exists(qr_output):
            qr = qrcode.make(qr_content)
            qr.save(qr_output)

        # Crear PDF
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)

        pdf.cell(200, 10, txt="Ticket de Turno", ln=True, align='C')
        pdf.cell(200, 10, txt=f"Nombre Completo: {data['nombre_completo']}", ln=True, align='L')
        pdf.cell(200, 10, txt=f"CURP: {data['curp']}", ln=True, align='L')
        pdf.cell(200, 10, txt=f"No Turno: {data['no_turno']}", ln=True, align='L')
        pdf.cell(200, 10, txt=f"Teléfono: {data['telefono']}", ln=True, align='L')
        pdf.cell(200, 10, txt=f"Celular: {data['celular']}", ln=True, align='L')
        pdf.cell(200, 10, txt=f"Correo: {data['correo']}", ln=True, align='L')
        pdf.cell(200, 10, txt=f"Nivel: {data['nivel']}", ln=True, align='L')
        pdf.cell(200, 10, txt=f"Municipio: {data['municipio']}", ln=True, align='L')
        pdf.cell(200, 10, txt=f"Asunto: {data['asunto']}", ln=True, align='L')

        pdf.image(qr_output, x=10, y=150, w=50)

        pdf.output(pdf_output)

        # URL del PDF
        pdf_url = url_for('static', filename=f'pdf/{os.path.basename(pdf_output)}', _external=True)

        return jsonify({'success': True, 'pdf_url': pdf_url})

    except Exception as e:
        print(f"Error al generar el PDF: {e}")
        return jsonify({'success': False, 'message': str(e)})
 
if __name__ == '__main__':
    app.run(debug=True)
    