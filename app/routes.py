from app import app
from flask import render_template, redirect, url_for
from app.models import Cliente
from app.forms import ClienteForm

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro_cliente():
    form = ClienteForm()
    if form.validate_on_submit():
        form.save()
        return redirect(url_for('homepage'))
    
    return render_template('cadastro.html', form=form)