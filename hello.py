from flask import Flask, redirect, request
from flask import render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)

bootstrap = Bootstrap(app)

@app.route('/')
def index():
    user_agente = request.headers.get('User-Agente')
    return render_template('index.html', user_agente = user_agente)


@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)

@app.route('/debian')
def debian():
    return redirect('https://www.debian.org/index.pt.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

