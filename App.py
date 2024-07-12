from flask import Flask, render_template, url_for, request, redirect, jsonify, send_file
from model.package_model.Usuario import Usuarios
from model.package_model.Formulario import Formulario
import os
import qrcode
from fpdf import FPDF


app = Flask(__name__)
app.secret_key = 'keykey'

HCAPTCHA_SECRET = 'ES_ef2fbcaf50b4434f9d9b9d05d4cd6ae3'

@app.route('/')
def index():
    return render_template('Index.html')

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


@app.route('/logout')
def logout():
    return redirect(url_for('index'))

@app.route('/admin_logout')
def admin_logout():
    return redirect(url_for('login'))

@app.route('/admin')
def admin():

    formulario_model = Formulario()
    forms = formulario_model.obtener_formularios()
    return render_template('admin.html', forms=forms)

@app.route('/generar_ticket', methods=['POST'])
def generar_ticket():
    if request.method == 'POST':
        return redirect(url_for('ticket', **request.form.to_dict()))

    return redirect(url_for('index'))

@app.route('/ticket')
def ticket():
    return render_template('Ticket.html', data=request.args.to_dict())

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