from flask import Flask, render_template, url_for, request, redirect, jsonify
from model.package_model.Usuario import Usuarios

app = Flask(__name__)
app.secret_key = 'keykey'


@app.route('/')
def index():
    return render_template('Index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.is_json:
            # Si la solicitud es JSON (enviado desde fetch en JavaScript)
            data = request.get_json()
            usuario = data.get('f_user')
            contrasena = data.get('f_pwd')
        else:
            # Si no es JSON, intenta obtener los datos del formulario HTML estándar
            usuario = request.form.get('f_user')
            contrasena = request.form.get('f_pwd')
        
        usuario_model = Usuarios()
        user = usuario_model.verificar_credenciales(usuario, contrasena)

        if user:
            return jsonify({'redirect': url_for('admin')})
        else:
            return jsonify({'message': 'Usuario o contraseña incorrectos'})

    # Si es GET, renderiza la plantilla de inicio de sesión (login.html)
    return render_template('login.html')


@app.route('/logout')
def logout():
    return redirect(url_for('index'))

@app.route('/admin')
def admin():
    return render_template('admin.html')

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