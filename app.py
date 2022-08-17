
import datetime
import sqlite3
import db.scripts as scripts
from werkzeug.security import generate_password_hash, check_password_hash

from flask import Flask, jsonify, render_template, request, redirect, url_for, session, escape

app = Flask(__name__, static_url_path='/static')
app.secret_key = 'palabra clave'


# Almacenamiento temporal de datos de reserva
booking_entries = []
review_entries = []


@app.route('/test/')
def hello():
    return "<h1>Hello, Esclavos del grupo 05 de MinTic Uninorte!!</h1>"


@app.before_request
def before_request():
    if 'usuario' not in session and request.endpoint in ['user', 'realizar_Comentario', 'booking', 'users', 'admin_users', 'editUser', 'editReserveAdmin', 'editReviewAdmin', 'admin_admins', 'addAdmin', 'editAdmin', 'admins_home']:
        return redirect('/')
    elif 'usuario' in session and (scripts.tipo_usuario_sesion_abierta == 1) and request.endpoint in ['admin_users', 'editReserveAdmin', 'editReviewAdmin', 'admin_admins', 'addAdmin', 'editAdmin', 'admins_home']:
        return redirect('/user')
    elif 'usuario' in session and (scripts.tipo_usuario_sesion_abierta == 2) and request.endpoint in ['admin_admins']:
        return redirect('/admin-rooms')


# @app.route('/base/')
# def base():
#     return render_template("base.html")


@app.route('/login', methods=['POST'])
def login():
    usuario = request.form.to_dict(flat=True)
    usuario_bd = scripts.obtener_usuario_login(usuario)
    if usuario_bd:
        valid_pass = check_password_hash(usuario_bd[8], usuario['contrasena'])
        if valid_pass:
            session['usuario'] = usuario_bd
            scripts.id_usuario_sesion = usuario_bd[0]
            print(scripts.id_usuario_sesion)
            scripts.tipo_usuario_sesion_abierta = usuario_bd[7]
            return redirect('/admin-admins')
        else:
            return redirect('/')
    else:
        return redirect('/')


@app.route('/cerrar-sesion')
def cerrar_sesion():
    session.pop('usuario', None)
    scripts.tipo_usuario_sesion_abierta = 0
    scripts.id_usuario_sesion = 0
    return redirect('/')


@app.route('/', methods=["GET", "POST"])
def home():
    if request.method == "POST":
        print(scripts.id_usuario_sesion)
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
    # if request.method == 'GET':
    #     reserva = request.form.to_dict(flat=True)
    #     print(reserva)
    #     # comentario = scripts.obtener_comentario_admin_id(id)
    #     return render_template('reservas.html', reserva=reserva)
    # else:
    reserva = request.form.to_dict(flat=True)
    print(scripts.id_usuario_sesion)
    # review = request.form.get("review-content")
    # rating = request.form.get("rate")
    # formatted_date = datetime.datetime.today().strftime("%Y-%m-%d")
    # review_entries.append((rating, review, formatted_date))

    # entries_with_date = [
    #     (
    #         entry[0],
    #         entry[1],
    #         entry[2],
    #         datetime.datetime.strptime(
    #             entry[2], "%Y-%m-%d").strftime("%b %d")
    #     )
    #     for entry in review_entries
    # ]

    # print(entries_with_date)

    # return render_template("reservas.html", reserva=reserva, review_entries=entries_with_date)
    return render_template("reservas.html", reserva=reserva)


@ app.route('/successful-booking/', methods=["POST"])
def successful_Booking():
    reserva = request.form.to_dict(flat=True)
    if request.form['gestion_usuario'] == 'Reservar':
        # print(scripts.id_usuario_sesion)
        scripts.reservar(scripts.id_usuario_sesion, reserva)

        ultimoIdReserva = (scripts.obtener_ultima_reserva())[0]
        print(ultimoIdReserva)

        for i in range(int(reserva['Habitaciones'])):
            scripts.reservar_detalle(
                i+1, ultimoIdReserva, reserva['PrecioTotalHabitacion'])
            # print(i+1)

        # for i=1 range(numero de habitaciones+1)
        #     scripts.reservar_detalle(id_room, id_reserva, precio_total_por_habitacion)
        #     scripts.reservar_detalle(i, ultimoIdReserva, reserva['PrecioTotalHabitacion'])

        return render_template("successfulBooking.html")
    else:
        return redirect('/')


@ app.route('/realizarComentario/', methods=["POST", "GET"])
def realizar_Comentario():
    if request.method == "GET":
        return render_template("comentarios.html")
    else:
        comentario = request.form.to_dict(flat=True)
        # review = request.form.get("review-content")
        # rating = request.form.get("rate")
        formatted_date = datetime.datetime.today().strftime("%Y-%m-%d")
        scripts.insertar_comentario(
            scripts.id_usuario_sesion, formatted_date, comentario)
        # print(formatted_date)
        # print(scripts.id_usuario_sesion)
        # print(comentario)
    #     review_entries.append((rating, review, formatted_date))

    # entries_with_date = [
    #     (
    #         entry[0],
    #         entry[1],
    #         entry[2],
    #         datetime.datetime.strptime(
    #             entry[2], "%Y-%m-%d").strftime("%b %d")
    #     )
    #     for entry in review_entries
    # ]

    # print(entries_with_date)

    # return render_template("comentarios.html", review_entries=entries_with_date)
        return redirect("/realizarComentario/")


@ app.route('/user/', methods=['POST', 'GET'])
def user():
    if request.method == 'GET':
        usuario = scripts.obtener_usuario_id(scripts.id_usuario_sesion)
        reservas = scripts.obtener_reservas_tabla_usuarioId(
            scripts.id_usuario_sesion)
        comentarios = scripts.obtener_comentarios_tabla_usuarioId(
            scripts.id_usuario_sesion)
        return render_template("users.html", usuario=usuario, reservas=reservas, comentarios=comentarios)
    else:
        usuario = request.form.to_dict(flat=True)
        usuario['Nueva_Contrasena'] = generate_password_hash(
            usuario['Nueva_Contrasena'])
        scripts.editar_usuario(scripts.id_usuario_sesion, usuario)
        return redirect('/user/')

# Edición de comentario user


@ app.route('/editarReview/<int:id>', methods=['POST', 'GET'])
def editReview(id):
    if request.method == 'GET':
        comentario = scripts.obtener_comentario_admin_id(id)
        return render_template('editarReview.html', comentario=comentario)
    else:
        comentario = request.form.to_dict(flat=True)
        if request.form['gestion_comentario_admin'] == 'Editar Comentario':
            scripts.editar_comentario_admin_id(id, comentario)
        elif request.form['gestion_comentario_admin'] == 'Eliminar Comentario':
            scripts.eliminar_comentario_admin_id(id)
        return redirect('/user')


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
        if request.form['gestion_usuario'] == 'Editar':
            usuario['Nueva_Contrasena'] = generate_password_hash(
                usuario['Nueva_Contrasena'])
            scripts.editar_usuario(id, usuario)
        elif request.form['gestion_usuario'] == 'Eliminar':
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
        usuario['Nueva_Contrasena'] = generate_password_hash(
            usuario['Nueva_Contrasena'])
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
        if request.form['gestion_usuario'] == 'Editar':
            # usuario=request.form.to_dict(flat=True)
            usuario['Nueva_Contrasena'] = generate_password_hash(
                usuario['Nueva_Contrasena'])
            scripts.editar_usuario(id, usuario)
        elif request.form['gestion_usuario'] == 'Eliminar':
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


@ app.route('/admin-rooms/', methods=["POST", "GET"])
def admins_home():
    if request.method == 'GET':
        habitaciones = scripts.obtener_habitacion_tabla()
        return render_template("gestionHabitaciones.html", habitaciones=habitaciones)
    else:
        cantidad_habitaciones = int(request.form['numero_habitaciones'])
        for i in range(cantidad_habitaciones):
            scripts.agregar_habitacion()

        return redirect('/admin-rooms')

        # for i in range(int(reserva['Habitaciones'])):
        #     scripts.reservar_detalle(i+1, ultimoIdReserva, reserva['PrecioTotalHabitacion'])


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
        usuario['Nueva_Contrasena'] = generate_password_hash(
            usuario['Nueva_Contrasena'])
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
