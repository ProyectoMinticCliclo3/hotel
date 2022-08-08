import datetime

from flask import Flask, render_template, request, redirect, url_for


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


@ app.route('/user/<name>')
def user(name):
    return render_template("users.html", name=name)


@ app.route('/admin/')
def admins_home():
    return render_template("homeadmin.html")


@ app.route('/admin-users/')
def admin_users():
    return render_template("gestionUsuarios.html")


@ app.route('/admin-admins/')
def admin_admins():
    return render_template("gestionAdministradores.html")


@ app.route('/contact/')
def contact():
    return render_template("contacto.html")


@ app.route('/about/')
def about():
    return render_template("nosotros.html")


@ app.route('/rooms/')
def rooms():
    return render_template("habitaciones.html")


@ app.route('/register/')
def register():
    return render_template("registro.html")


# if __name__ == '__main__':
#     app.run(port=4995)
