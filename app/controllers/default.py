from flask import render_template, flash, redirect, url_for
from flask_login import login_user, logout_user
from app import app, db, login_manager

from app.models.tables import User
from app.models.forms import LoginForm


@login_manager.user_loader
def load_user(user_id):
    # since the user_id is just the primary key of our user table, use it in the query for the user
    return User.query.get(int(user_id))


@app.route('/index/')
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login/', methods=["GET", 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.password == form.password.data:
            login_user(user)
            flash('Logged in.')
            return redirect(url_for("index"))
        else:
            flash('Usuário e/ou senha inválido')
        #endif
    #endif
    return render_template('login.html', form=form)


@app.route("/logout")
def logout():
    logout_user()
    flash('Logged out.')
    return redirect(url_for("index"))


#
'''
@app.route('/test/<info>')
@app.route("/test/", defaults={'info': None})
def test(info):
    r = User.query.filter_by(username='admin').first()
    #r = User.query.filter(User.password.endswith('admin')).all()
    #print(r.username, r.name)
    print(r.username, r.name)
    return "OK"

@app.route('/test/<info>')
@app.route("/test/", defaults={'info': None})
def test(info):
    i = User('admin', 'admin', 'Adminintrador', 'admin@toilter.com.br')
    db.session.add(i)
    db.session.commit()
    return "Ok"
@app.route("/test/", defaults={'name': None})
@app.route("/test/<name>")
def test(name):
    if name: 
        return "Olá, %s!" % name
    else:
        return "Olá, usuário!"

@app.route("/test2/<int:id>")
def test2(id):    
    print (type(id))
    return str(id)

@app.route("/test3/", methods=['GET'])
def test3():    
    return "Oi!"
'''