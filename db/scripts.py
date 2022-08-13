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
