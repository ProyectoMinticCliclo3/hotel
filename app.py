from flask import Flask, render_template
app = Flask(__name__, static_url_path='/static')


@app.route('/test/')
def hello():
    return "Hello, Flask"


@app.route('/')
def home():
    return render_template("base.html")


@app.route('/index/')
def index():
    return render_template("index.html")


@app.route('/usuarios/')
def users():
    return render_template("users.html")


@app.route('/admins/')
def admins_home():
    return render_template("homeadmin.html")


@app.route('/admins-usuarios/')
def admins_users():
    return render_template("gestionUsuarios.html")


@app.route('/admins-admins/')
def admins_admins():
    return render_template("gestionAdministradores.html")


@app.route('/contacto/')
def contact():
    return render_template("contacto.html")


if __name__ == '__main__':
    app.run()
