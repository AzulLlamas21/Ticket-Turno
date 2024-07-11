from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__)


#@app.route('/')
#def index():
#    return 'Hello, Word!'

@app.route('/')
def index():
    return render_template('Index.html')

@app.route('/login')
def login():
    return render_template('login.html')

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