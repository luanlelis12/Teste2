from flask import Flask, render_template
from flask-sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///DB.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(30), unique=True, nullable=False)
    senha = db.Column(db.String(30), unique=True, nullable=False)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/Login')
def login():
    return render_template('login.html')

@app.route('/Cadastro')
def cadastro():
    return render_template('cadastro.html')

if __name__ == '__main__':
    app.run(debug=True)