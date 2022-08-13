
import datetime
import sqlite3
import db.scripts as scripts
from werkzeug.security import generate_password_hash

from flask import Flask, jsonify, render_template, request, redirect, url_for


app = Flask(__name__, static_url_path='/static')

# Almacenamiento temporal de datos de reserva
booking_entries = []
review_entries = []


@app.route('/test/')
def hello():
    return "<h1>Hello, Esclavos del grupo 05 de MinTic Uninorte!!</h1>"


@app.route('/base/')
def base():
    return render_template("base.html")


@app.route('/', methods=["GET", "POST"])
def home():
    if request.method == "POST":
        # Obtiene fecha de hoy para referencia
        formatted_date = datetime.datetime.today().strftime("%Y-%m-%d")
        check_in = request.form.get("check-in")
        check_out = request.form.get("check-out")
        num_guest = request.form.get("huespedes")
        num_room = request.form.get("habitaciones")

        args = {"formatted_date": formatted_date, "check_in": check_in,
                "check_out": check_out, "num_guest": num_guest, "num_room": num_room}

        booking_entries.append(args)

        print(formatted_date, check_in, check_out, num_guest, num_room)
        print(booking_entries)
        return redirect(url_for('booking'))
    return render_template("index.html", booking_entries=booking_entries)


@ app.route('/booking/', methods=["GET", "POST"])
def booking():
    if request.method == "POST":
        review = request.form.get("review-content")
        rating = request.form.get("rate")
        formatted_date = datetime.datetime.today().strftime("%Y-%m-%d")
        review_entries.append((rating, review, formatted_date))

    entries_with_date = [
        (
            entry[0],
            entry[1],
            entry[2],
            datetime.datetime.strptime(
                entry[2], "%Y-%m-%d").strftime("%b %d")
        )
        for entry in review_entries
    ]

    print(entries_with_date)

    return render_template("reservas.html", review_entries=entries_with_date)


@ app.route('/user/')
def user():
    return render_template("users.html")


@ app.route('/admin-users/')
def admin_users():
    usuarios = scripts.obtener_usuario_tabla(1)
    reservas = scripts.obtener_reservas_tabla()
    comentarios = scripts.obtener_comentarios_tabla()
    return render_template("gestionUsuarios.html", usuarios=usuarios, reservas=reservas, comentarios=comentarios)


# Edición de usuario cliente
@ app.route('/editarUser/<int:id>', methods=['POST', 'GET'])
def editUser(id):
    if request.method == 'GET':
        usuario = scripts.obtener_usuario_id(id)
        return render_template('editarUser.html', usuario=usuario)
    else:
        usuario = request.form.to_dict(flat=True)
        if request.form['gestion_usuario'] == 'Editar Usuario':
            # usuario=request.form.to_dict(flat=True)
            scripts.editar_usuario(id, usuario)
        elif request.form['gestion_usuario'] == 'Eliminar Usuario':
            # usuario=request.form.to_dict(flat=True)
            scripts.eliminar_usuario(id)
        return redirect('/admin-users')

# Edición de reserva cliente
@ app.route('/eliminarReserveAdmin/<int:id>', methods=['POST', 'GET'])
def editReserveAdmin(id):
    if request.method == 'GET':
        reserva = scripts.obtener_reserva_admin_id(id)
        return render_template('eliminarReserveAdmin.html', reserva=reserva)
    else:
        reserva = request.form.to_dict(flat=True)
        # if request.form['gestion_usuario'] == 'Editar Usuario':
        #     # usuario=request.form.to_dict(flat=True)
        #     scripts.editar_usuario(id, usuario)
        if request.form['gestion_reserva_admin'] == 'Eliminar Reserva':
            # usuario=request.form.to_dict(flat=True)
            scripts.eliminar_reserva_admin_id(id)
        return redirect('/admin-users')

# Edición de comentario admin
@ app.route('/eliminarReviewAdmin/<int:id>', methods=['POST', 'GET'])
def editReviewAdmin(id):
    if request.method == 'GET':
        comentario = scripts.obtener_comentario_admin_id(id)
        return render_template('eliminarReviewAdmin.html', comentario=comentario)
    else:
        comentario = request.form.to_dict(flat=True)
        if request.form['gestion_comentario_admin'] == 'Eliminar Comentario':
            scripts.eliminar_comentario_admin_id(id)
        return redirect('/admin-users')


@ app.route('/admin-admins/')
def admin_admins():
    usuarios = scripts.obtener_usuario_tabla(2)
    return render_template("gestionAdministradores.html", usuarios=usuarios)

# Creacion de usuario administrador


@ app.route('/addAdmin', methods=['POST'])
def addAdmin():
    if request.form['gestion_admin'] == 'Crear Admin':
        usuario = request.form.to_dict(flat=True)
        usuario['Nueva_Contrasena'] = generate_password_hash(usuario['Nueva_Contrasena'])
        scripts.insertar_usuario(usuario)
        # return jsonify(usuario)
    return redirect('/admin-admins')


# Edición de usuario administrador
@ app.route('/editarAdmin/<int:id>', methods=['POST', 'GET'])
def editAdmin(id):
    if request.method == 'GET':
        usuario = scripts.obtener_usuario_id(id)
        return render_template('editarAdmin.html', usuario=usuario)
    else:
        usuario = request.form.to_dict(flat=True)
        if request.form['gestion_usuario'] == 'Editar Admin':
            # usuario=request.form.to_dict(flat=True)
            scripts.editar_usuario(id, usuario)
        elif request.form['gestion_usuario'] == 'Eliminar Admin':
            # usuario=request.form.to_dict(flat=True)
            scripts.eliminar_usuario(id)
        return redirect('/admin-admins')

    # if request.form['gestion_admin'] == 'Editar Admin':
    #     usuario=request.form.to_dict(flat=True)
    #     scripts.insertar_usuario(usuario)
        # return jsonify(usuario)
    # return redirect('/admin-admins')


@ app.route('/contact/')
def contact():
    return render_template("contacto.html")


@ app.route('/about/')
def about():
    return render_template("nosotros.html")


@ app.route('/rooms/')
def rooms():
    return render_template("habitaciones.html")


@ app.route('/admin-rooms/')
def admins_home():
    habitaciones = scripts.obtener_habitacion_tabla()
    return render_template("gestionHabitaciones.html", habitaciones=habitaciones)


# @ app.route('/addRoom', methods=['POST'])
# def add_room():
#     if request.form['gestion_admin'] == 'Crear Admin':
#         usuario = request.form.to_dict(flat=True)
#         scripts.insertar_usuario(usuario)
#         # return jsonify(usuario)
#     return redirect('/admin-rooms')


@app.route('/register')
def register():
    usuarios = scripts.obtener_usuario_tabla(2)
    return render_template("registro.html", usuarios=usuarios)


@ app.route('/registerNew', methods=['POST'])
def register_new():
    if request.form['botonConfirm'] == 'Confirmar':
        usuario = request.form.to_dict(flat=True)
        usuario['Nueva_Contrasena'] = generate_password_hash(usuario['Nueva_Contrasena'])
        scripts.insertar_usuario(usuario)
    return redirect("/booking/")


# @ app.route('/addAdmin', methods=['POST'])
# def addAdmin():
#     if request.form['gestion_admin'] == 'Crear Admin':
#         usuario = request.form.to_dict(flat=True)
#         scripts.insertar_usuario(usuario)
#         # return jsonify(usuario)
#     return redirect('/admin-admins')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
# if __name__ == '__main__':
#     app.run(port=4995)
