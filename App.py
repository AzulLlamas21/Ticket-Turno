from flask import Flask, render_template, url_for, request, redirect, jsonify
from model.package_model.Usuario import Usuarios
from model.package_model.Formulario import Formulario

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

if __name__ == '__main__':
    app.run(debug=True)