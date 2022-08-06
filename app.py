from flask import Flask, render_template


app = Flask(__name__, static_url_path='/static')


@app.route('/test/')
def hello():
    return "Hello, Flask"


@app.route('/')
def base():
    return render_template("base.html")


@app.route('/home/')
def home():
    return render_template("index.html")


@app.route('/user/')
def user():
    return render_template("users.html")


@app.route('/admin/')
def admins_home():
    return render_template("homeadmin.html")


@app.route('/admin-users/')
def admin_users():
    return render_template("gestionUsuarios.html")


@app.route('/admin-admins/')
def admin_admins():
    return render_template("gestionAdministradores.html")


@app.route('/contact/')
def contact():
    return render_template("contacto.html")


@app.route('/about/')
def about():
    return render_template("nosotros.html")


@app.route('/booking/')
def booking():
    return render_template("reservas.html")


@app.route('/rooms/')
def rooms():
    return render_template("habitaciones.html")


@app.route('/register/')
def register():
    return render_template("registro.html")


if __name__ == '__main__':
    app.run(port=4995)
