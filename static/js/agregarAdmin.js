

const btn_AgregarAdmin = document.getElementById('btnAgregarAdmin')

const table_admins = document.getElementById('table_admins')

const form_agregarAdmin = document.querySelector('#form_dataUser')

const btn_cancelarAgregarAdmin = document.getElementById('cancel_user')

btn_AgregarAdmin.addEventListener('click', () =>{
    btn_AgregarAdmin.style.cssText='display:none'
    table_admins.style.cssText = 'display:none'
    form_agregarAdmin.style.cssText = 'display:block'
})

btn_cancelarAgregarAdmin.addEventListener('click', () =>{
    btn_AgregarAdmin.style.cssText='display:block'
    table_admins.style.cssText = 'display:block'
    form_agregarAdmin.style.cssText = 'display:none'
})

// const btn_eliminar_comentario_admin = document.getElementById('eliminar_comentario')
// btn_eliminar_comentario_admin.addEventListener('click', () =>{
    
// })


const btn_cerrarSesion = document.getElementById('cerrar_sesion')
if (btn_cerrarSesion){
    btn_cerrarSesion.addEventListener('click', () =>{
        console.log("holaaaaa")
        fetch('/cerrar-sesion')
        .then(res => window.location.href = "/")
        .catch(error => console.log(error))
    })
}