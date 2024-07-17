from flask import Flask, render_template, url_for, request, redirect, jsonify, send_file
from model.db import db
from model.package_model.Usuario import Usuarios
from model.package_model.Formulario import Formulario
from model.package_model.Nivel import Nivel
from  model.package_model.Municipio import Municipio
from model.package_model.Asunto import Asunto
import os
import qrcode
import matplotlib.pyplot as plt
import io
import base64
import pandas as pd
from fpdf import FPDF
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

HCAPTCHA_SECRET = 'ES_ef2fbcaf50b4434f9d9b9d05d4cd6ae3'


#INDEX
@app.route('/')
def index():
    obj_nv = Nivel.Nivel()
    obj_mun = Municipio.Municipio()
    obj_asu = Asunto.Asunto()
    lista_niveles = obj_nv.obtener_niveles()
    lista_municipios = obj_mun.obtener_municipios()
    lista_asuntos = obj_asu.obtener_asuntos()
    return render_template('Index.html', lista_niveles=lista_niveles, lista_municipios=lista_municipios, lista_asuntos=lista_asuntos)

#LOGIN
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.is_json:
            data = request.get_json()
            print(data, '\n\n\n')
            usuario = data.get('f_user')
            contrasena = data.get('f_pwd')
        else:
            usuario = request.form.get('f_user')
            contrasena = request.form.get('f_pwd')
        
        usuario_model = Usuarios()
        user = usuario_model.verificar_credenciales(usuario, contrasena)

        if user:
            return jsonify({'redirect': url_for('admin')})
        else:
            return jsonify({'message': 'Usuario o contraseña incorrectos'})

    return render_template('login.html')

#CERRAR Y REGRESAR A INDEX
@app.route('/logout')
def logout():
    return redirect(url_for('index'))

#CERRAR Y REGRESAR A LOGIN
@app.route('/admin_logout')
def admin_logout():
    return redirect(url_for('login'))

#ADMINISTRADOR(OBTENER LISTA DE FORMULARIO)
@app.route('/admin')
def admin():
    formulario_model = Formulario()
    forms = formulario_model.obtener_formularios()
    return render_template('admin.html', forms=forms)

#IR A DASHBOARD
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

#DASHBOARD
@app.route('/dashboard/data')
def dashboard_data():
    municipio = request.args.get('municipio')
    formulario_model = Formulario()
    if municipio:
        forms = formulario_model.obtener_formularios_por_municipio(municipio)
    else:
        forms = formulario_model.obtener_formularios()
    
    df = pd.DataFrame(forms, columns=['no_turno', 'curp', 'nombre', 'paterno', 'materno', 'telefono', 'celular', 'correo', 'id_nivel', 'id_mun', 'id_asunto', 'estado'])
    estado_counts = df['estado'].value_counts()
    
    plt.figure(figsize=(10, 6))
    estado_counts.plot(kind='bar', color=['green', 'blue', 'red'])
    plt.title('Estado de Solicitudes')
    plt.xlabel('Estado')
    plt.ylabel('Cantidad')

    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    image_base64 = base64.b64encode(buf.getvalue()).decode('utf-8')
    buf.close()

    return jsonify({'image': 'data:image/png;base64,{}'.format(image_base64)})

@app.route('/buscar_formulario')
def buscar_formulario():
    query = request.args.get('query')
    # Realiza la búsqueda en la base de datos y devuelve el formulario correspondiente
    formulario = Formulario.query.filter((Formulario.curp == query) | (Formulario.nombre_completo == query)).first()
    if formulario:
        return jsonify(success=True, formulario=formulario.to_dict())
    return jsonify(success=False)

@app.route('/agregar_formulario', methods=['POST'])
def agregar_formulario():
    data = request.get_json()
    # Agrega el formulario a la base de datos
    nuevo_formulario = Formulario(**data)
    db.session.add(nuevo_formulario)
    db.session.commit()
    return jsonify(success=True)

@app.route('/actualizar_formulario', methods=['PUT'])
def actualizar_formulario():
    data = request.get_json()
    # Actualiza el formulario en la base de datos
    formulario = Formulario.query.filter_by(curp=data['curp']).first()
    if formulario:
        for key, value in data.items():
            setattr(formulario, key, value)
        db.session.commit()
        return jsonify(success=True)
    return jsonify(success=False)

@app.route('/eliminar_formulario', methods=['DELETE'])
def eliminar_formulario():
    curp = request.args.get('curp')
    # Elimina el formulario de la base de datos
    formulario = Formulario.query.filter_by(curp=curp).first()
    if formulario:
        db.session.delete(formulario)
        db.session.commit()
        return jsonify(success=True)
    return jsonify(success=False)


#GENERAR TICKET
@app.route('/generar_ticket', methods=['POST'])
def generar_ticket():
    try:
        # Recoger los datos del formulario
        f_nc = request.form['f_nc']
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
            id_nivel=f_nivel, id_mun=f_mun, id_asunto=f_asunto, estado='pendiente'
        )
        # Agregar a la sesión y confirmar
        db.session.add(nuevo_formulario)
        db.session.commit()
        
        # Datos a pasar a la plantilla
        datos = {
            'nombre_completo': f_nc,
            'curp': f_curp,
            'nombre': f_nombre,
            'paterno': f_paterno,
            'materno': f_materno,
            'telefono': f_telefono,
            'celular': f_celular,
            'correo': f_correo,
            'nivel': f_nivel,
            'municipio': f_mun,
            'asunto': f_asunto
        }
        
        return render_template('Ticket.html', datos=datos)
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
    data = request.json
    pdf_dir = os.path.join(app.root_path, 'static', 'pdf')
    qr_dir = os.path.join(app.root_path, 'static', 'qr')
    if not os.path.exists(pdf_dir):
        os.makedirs(pdf_dir)
    if not os.path.exists(qr_dir):
        os.makedirs(qr_dir)
    
    existing_files = os.listdir(pdf_dir)
    for file in existing_files:
        if data['curp'] in file and data['asunto'] in file:
            pdf_filename = file
            pdf_url = url_for('static', filename=f'pdf/{pdf_filename}', _external=True)
            return jsonify({'success': True, 'pdf_url': pdf_url})
    
    no_turno = 1
    if existing_files:
        existing_numbers = [int(f.split('-')[0]) for f in existing_files if '-' in f]
        if existing_numbers:
            no_turno = max(existing_numbers) + 1

    pdf_filename = f"{no_turno}-{data['curp']}-{data['asunto']}.pdf"
    pdf_output = os.path.join(pdf_dir, pdf_filename)
    
    qr_content = f"CURP: {data['curp']}, No Turno: {no_turno}"
    qr_image = qrcode.make(qr_content)
    qr_filename = f"{no_turno}-{data['curp']}-{data['asunto']}.png"
    qr_output = os.path.join(qr_dir, qr_filename)
    qr_image.save(qr_output)
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, txt="Ticket de Turno", ln=True, align='C')
    pdf.ln(10)
    pdf.cell(200, 10, txt=f"Nombre Completo: {data['nc']}", ln=True)
    pdf.cell(200, 10, txt=f"CURP: {data['curp']}", ln=True)
    pdf.cell(200, 10, txt=f"Nombre: {data['nombre']}", ln=True)
    pdf.cell(200, 10, txt=f"Apellido Paterno: {data['paterno']}", ln=True)
    pdf.cell(200, 10, txt=f"Apellido Materno: {data['materno']}", ln=True)
    pdf.cell(200, 10, txt=f"Teléfono: {data['telefono']}", ln=True)
    pdf.cell(200, 10, txt=f"Celular: {data['celular']}", ln=True)
    pdf.cell(200, 10, txt=f"Correo: {data['correo']}", ln=True)
    pdf.cell(200, 10, txt=f"Nivel: {data['nivel']}", ln=True)
    pdf.cell(200, 10, txt=f"Municipio: {data['municipio']}", ln=True)
    pdf.cell(200, 10, txt=f"Asunto: {data['asunto']}", ln=True)
    
    pdf.ln(10)
    pdf.image(qr_output, x = None, y = None, w = 50, h = 50)
    pdf.output(pdf_output)
    pdf_url = url_for('static', filename=f'pdf/{pdf_filename}', _external=True)

    return jsonify({'success': True, 'pdf_url': pdf_url})

if __name__ == '__main__':
    app.run(debug=True)
    