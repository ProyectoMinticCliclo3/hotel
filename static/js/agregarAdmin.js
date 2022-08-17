

const btn_AgregarAdmin = document.getElementById('btnAgregarAdmin')

const table_admins = document.getElementById('table_admins')

const form_agregarAdmin = document.querySelector('#form_dataUser')

const btn_cancelarAgregarAdmin = document.getElementById('cancel_user')

if(btn_AgregarAdmin){
    btn_AgregarAdmin.addEventListener('click', () =>{
        btn_AgregarAdmin.style.cssText='display:none'
        table_admins.style.cssText = 'display:none'
        form_agregarAdmin.style.cssText = 'display:block'
    })
}

if(btn_cancelarAgregarAdmin){
    btn_cancelarAgregarAdmin.addEventListener('click', () =>{
        btn_AgregarAdmin.style.cssText='display:block'
        table_admins.style.cssText = 'display:block'
        form_agregarAdmin.style.cssText = 'display:none'
    })
}

// const btn_eliminar_comentario_admin = document.getElementById('eliminar_comentario')
// btn_eliminar_comentario_admin.addEventListener('click', () =>{
    
// })


const btn_cerrarSesion = document.getElementById('cerrar_sesion')
if (btn_cerrarSesion){
    btn_cerrarSesion.addEventListener('click', () =>{
        fetch('/cerrar-sesion')
        .then(res => window.location.href = "/")
        .catch(error => console.log(error))
    })
}

const btn_fechaCheckIn = document.getElementById('Check-In-Booking')
const btn_fechaCheckOut = document.getElementById('Check-Out-Booking')
const valorTotal = document.getElementById('ValorTotal')
const btn_verDisponibilidad = document.getElementById('verDisponibilidad')
const cantidadNoches = document.getElementById('CantidadNoches')
const cantidadHabitaciones = document.getElementById('Habitaciones')
const precioTotalHabitacion = document.getElementById('PrecioTotalHabitacion')
if (btn_verDisponibilidad){
    btn_verDisponibilidad.addEventListener('click', () =>{
        console.log(btn_fechaCheckOut.value)
        var fechaCheckIn = new Date(btn_fechaCheckIn.value).getTime();
        var fechaCheckOut= new Date(btn_fechaCheckOut.value).getTime(); 
        var cantidad_dias = (fechaCheckOut-fechaCheckIn)/(1000*60*60*24);
        cantidadNoches.value = cantidad_dias
        precioTotalHabitacion.value = (cantidad_dias*450000)
        valorTotal.value = (cantidad_dias*450000)*cantidadHabitaciones.value;
    })
}
