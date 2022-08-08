// TODO FIX HERE
// var modal = document.getElementById("modal-id01");
// window.onclick = function (event) {
//   if (event.target == modal) {
//     modal.style.display = "none";
//   }
// };
<<<<<<< HEAD:js/sidebar.js
var modal = document.querySelector(".modal");
window.onclick = function (event) {
  if (event.target == modal) {
    modal.style.display =  "none";
  }
};
=======
>>>>>>> 43c8b59d6c7b60d623183800d8f3d8f54193d3c8:static/js/modal.js

// var modal = document.getElementById("modal-id02");
// window.onclick = function (event) {
//   if (event.target == modal) {
//     modal.style.display = "none";
//   }
// };

// FIXME
const openEls = document.querySelectorAll("[data-open]");
// const closeEls = document.querySelectorAll("[data-close]");
const isVisible = "is-visible";

for (const el of openEls) {
  el.addEventListener("click", function () {
    const modalId = this.dataset.open;
    document.getElementById(modalId).classList.add(isVisible);
  });
}
// FIXME END

// LEER MODAL BOX
var modal = document.querySelector(".modal");

// LEER BOTON MODAL
var btn = document.getElementsByClassName(".modal-btn");

// ABRIR MODAL BOX
function openModal() {
  modal.style.display = "block";
}
// FUNCION CERRAR MODAL
function closeModal() {
  modal.style.display = "none";
}

// CERRAR EN ESCAPE
document.addEventListener("keyup", (e) => {
  // if we press the ESC
  if (e.key == "Escape" && document.querySelector(".modal.is-visible")) {
    closeModal();
  }
});

// // ABRIR ON CLICK A BOTON
btn.onclick = function () {
  openModal();
};

// CERRAR MODAL SI CLICK AFUERA
window.onclick = function (event) {
  if (event.target == modal) {
    closeModal();
  }
};

// document.addEventListener(
//   "click",
//   function (event) {
//     // If user either clicks X button OR clicks outside the modal window, then close modal by calling closeModal()
//     if (
//       event.target.matches(".modal-cancelbtn") ||
//       !event.target.closest(".modal")
//     ) {
//       closeModal();
//     }
//   },
//   false
// );

// for (const el of closeEls) {
//   el.addEventListener("click", function () {
//     this.parentElement.parentElement.parentElement.classList.remove(isVisible);
//   });
// }

// document.addEventListener("click", (e) => {
//   if (e.target == document.querySelector(".modal.is-visible")) {
//     document.querySelector(".modal.is-visible").classList.remove(isVisible);
//   }
// });

// document.addEventListener("keyup", e => {
//   // if we press the ESC
//   if (e.key == "Escape" && document.querySelector(".modal.is-visible")) {
//     document.querySelector(".modal.is-visible").classList.remove(isVisible);
//   }
// });
