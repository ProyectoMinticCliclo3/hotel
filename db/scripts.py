import sqlite3


def conexion_bd():
    try:
        conexion = sqlite3.connect('db/dbHotel.db')
        return conexion
    except:
        print('Error de conexion bd')


def insertar_usuario(usuario):
    query = "insert into User (Cedula, Nombre, Apellidos, Fecha_Nacimiento, Correo, Celular, Tipo_Usuario, Contrasena) values ('{}','{}','{}','{}','{}','{}','{}','{}');".format(
        usuario['Cedula'], usuario['Nombre'], usuario['Apellidos'], usuario['Fecha_Nacimiento'], usuario['Correo'], usuario['Celular'], usuario['Tipo_Usuario'], usuario['Nueva_Contrasena'])
    # print(query)
    conexion = conexion_bd()
    # print(conexion)
    cursorObj = conexion.cursor()
    cursorObj.execute(query)
    conexion.commit()
    conexion.close()


id_usuario_sesion = 0
tipo_usuario_sesion_abierta = 0
# Para el login


def obtener_usuario_login(usuario):
    query = "select * from User where Correo='{}';".format(usuario['correo'])
    # print(query)
    conexion = conexion_bd()
    cursorObj = conexion.cursor()
    cursorObj.execute(query)
    usuario = cursorObj.fetchone()
    conexion.commit()
    conexion.close()
    return usuario

# Funciona para administradores y clientes gracias al parámetro tipo


def obtener_usuario_tabla(tipo):
    query = 'select Id, Cedula, Nombre, Apellidos, Fecha_Nacimiento, Correo, Celular, Tipo_Usuario, Contrasena from User where Tipo_Usuario={};'.format(
        tipo)
    # print(query)
    conexion = conexion_bd()
    cursorObj = conexion.cursor()
    usuarios = cursorObj.execute(query)
    usuarios = cursorObj.fetchall()
    conexion.commit()
    conexion.close()
    # print(usuarios)
    return usuarios


def obtener_usuario_id(id):
    query = 'select * from User where id={};'.format(id)
    # print(query)
    conexion = conexion_bd()
    cursorObj = conexion.cursor()
    cursorObj.execute(query)
    usuario = cursorObj.fetchone()
    conexion.commit()
    conexion.close()
    # print(usuarios)
    return usuario


def editar_usuario(id, usuario):
    query = "update User set Cedula='{}', Nombre='{}', Apellidos='{}', Fecha_Nacimiento='{}', Correo='{}', Celular='{}', Tipo_Usuario='{}', Contrasena='{}' where id = {};".format(
        usuario['Cedula'], usuario['Nombre'], usuario['Apellidos'], usuario['Fecha_Nacimiento'], usuario['Correo'], usuario['Celular'], usuario['Tipo_Usuario'], usuario['Nueva_Contrasena'], id)
    # print(query)
    conexion = conexion_bd()
    cursorObj = conexion.cursor()
    cursorObj.execute(query)
    conexion.commit()
    conexion.close()
    # print(usuarios)
    # return usuarios


def eliminar_usuario(id):
    query = "delete from User where id = {};".format(id)
    # print(query)
    conexion = conexion_bd()
    cursorObj = conexion.cursor()
    cursorObj.execute(query)
    conexion.commit()
    conexion.close()


def obtener_comentarios_tabla():
    query = 'select Id, Id_User, Fecha, Comentario from Reviews;'
    # print(query)
    conexion = conexion_bd()
    cursorObj = conexion.cursor()
    comentarios = cursorObj.execute(query)
    comentarios = cursorObj.fetchall()
    conexion.commit()
    conexion.close()
    # print(usuarios)
    return comentarios


def obtener_comentario_admin_id(id):
    query = 'select * from Reviews where id={};'.format(id)
    # print(query)
    conexion = conexion_bd()
    cursorObj = conexion.cursor()
    cursorObj.execute(query)
    comentario = cursorObj.fetchone()
    conexion.commit()
    conexion.close()
    return comentario


def eliminar_comentario_admin_id(id):
    query = "delete from Reviews where id = {};".format(id)
    # print(query)
    conexion = conexion_bd()
    cursorObj = conexion.cursor()
    cursorObj.execute(query)
    conexion.commit()
    conexion.close()


def editar_comentario_admin_id(id, comentario):
    query = "update Reviews set Comentario='{}' where id = {};".format(
        comentario['comentario'], id)
    # print(query)
    conexion = conexion_bd()
    cursorObj = conexion.cursor()
    cursorObj.execute(query)
    conexion.commit()
    conexion.close()


def obtener_reservas_tabla():
    query = 'select * from Reserva;'
    # print(query)
    conexion = conexion_bd()
    cursorObj = conexion.cursor()
    reservas = cursorObj.execute(query)
    reservas = cursorObj.fetchall()
    conexion.commit()
    conexion.close()
    # print(usuarios)
    return reservas


def obtener_reserva_admin_id(id):
    query = 'select * from Reserva where id={};'.format(id)
    # print(query)
    conexion = conexion_bd()
    cursorObj = conexion.cursor()
    cursorObj.execute(query)
    reserva = cursorObj.fetchone()
    conexion.commit()
    conexion.close()
    return reserva


def eliminar_reserva_admin_id(id):
    query = "delete from Reserva where id = {};".format(id)
    # print(query)
    conexion = conexion_bd()
    cursorObj = conexion.cursor()
    cursorObj.execute(query)
    conexion.commit()
    conexion.close()


def obtener_reservas_tabla_usuarioId(id_usuario):
    query = 'select * from Reserva where Id_User={};'.format(id_usuario)
    # print(query)
    conexion = conexion_bd()
    cursorObj = conexion.cursor()
    reservas = cursorObj.execute(query)
    reservas = cursorObj.fetchall()
    conexion.commit()
    conexion.close()
    # print(usuarios)
    return reservas


def obtener_comentarios_tabla_usuarioId(id_usuario):
    query = 'select Id, Id_User, Fecha, Comentario from Reviews where Id_User={};'.format(
        id_usuario)
    # print(query)
    conexion = conexion_bd()
    cursorObj = conexion.cursor()
    comentarios = cursorObj.execute(query)
    comentarios = cursorObj.fetchall()
    conexion.commit()
    conexion.close()
    # print(usuarios)
    return comentarios


# Funciona para administradores y clientes gracias al parámetro tipo


def obtener_habitacion_tabla():
    query = 'select * from Room;'
    # print(query)
    conexion = conexion_bd()
    cursorObj = conexion.cursor()
    habitaciones = cursorObj.execute(query)
    habitaciones = cursorObj.fetchall()
    conexion.commit()
    conexion.close()
    # print(usuarios)
    return habitaciones

# falta corregir lo que se inserta
def reservar(id_user, reserva):
    query = "insert into Reserva (Id_User, Fecha_Entrada, Fecha_Salida, CantidadPersonas) values ('{}','{}','{}','{}');".format(
        id_user, reserva['Check-In'], reserva['Check-Out'], reserva['Huespedes'])
    conexion = conexion_bd()
    # print(conexion)
    cursorObj = conexion.cursor()
    cursorObj.execute(query)
    conexion.commit()
    conexion.close()

# falta corregir lo que se inserta
# def reservar_detalle(reserva_realizada, reserva):
#     query = "insert into Detalle (Id_Room, Id_Reserva, Precio_Total_Room) values ('{}','{}','{}');".format(
#         1, reserva_realizada['Id'], reserva['PrecioTotalHabitacion'])
#     conexion = conexion_bd()
#     cursorObj = conexion.cursor()
#     detalle_reserva = cursorObj.execute(query)
#     detalle_reserva = cursorObj.fetchone()
#     conexion.commit()
#     conexion.close()
#     return detalle_reserva