from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Aldo'}
    interactions = [
        {
            'author': {'username': 'Aldo'},
            'body': 'Cliente llamo por telefono.'
        },
        {
            'author': {'username': 'Omar'},
            'body': 'cliente solicito cotizacion por whatsapp.'
        }
    ]
    return render_template('index.html', title='Home', user=user, interactions=interactions)