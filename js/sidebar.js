// SIDEBAR

// type = "module";
// src = "https://unpkg.com/ionicons@5.5.2/dist/ionicons/ionicons.esm.js";
// nomodule;
// src = "https://unpkg.com/ionicons@5.5.2/dist/ionicons/ionicons.js";

// // MenuToggle
// let toggle = document.querySelector(".toggle");
// let navigation = document.querySelector(".navigation");
// let main = document.querySelector(".main");

// toggle.onclick = function () {
//   navigation.classList.toggle("active");
//   main.classList.toggle("active");
// };
// //add hovered class in selected list item
// let list = document.querySelectorAll(".navigation li");
// list[1].classList.add("hovered"); //seleccionar el primero de la lista
// function activeLink() {
//   list.forEach((item) => item.classList.remove("hovered"));
//   this.classList.add("hovered");
// }
// list.forEach((item) => item.addEventListener("mouseover", activeLink));

function openNav() {
  document.getElementById("mySidebar").style.width = "14rem";
  document.getElementById("mainContent").style.marginLeft = "14rem";
}

function openOrClose(x) {
  if (x == 0) {
    openNav();
    openbtn.value = 1;
  } else {
    closeNav();
    openbtn.value = 0;
  }
}

function closeNav() {
  document.getElementById("mySidebar").style.width = "5rem";
  document.getElementById("mainContent").style.marginLeft = "5rem";
}
// TODO FIX HERE
// var modal = document.getElementById("modal-id01");
// window.onclick = function (event) {
//   if (event.target == modal) {
//     modal.style.display = "none";
//   }
// };
var modal = document.querySelector(".modal");
window.onclick = function (event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
};

// var modal = document.getElementById("modal-id02");
// window.onclick = function (event) {
//   if (event.target == modal) {
//     modal.style.display = "none";
//   }
// };

const openEls = document.querySelectorAll("[data-open]");
// const closeEls = document.querySelectorAll("[data-close]");
const isVisible = "is-visible";

for (const el of openEls) {
  el.addEventListener("click", function () {
    const modalId = this.dataset.open;
    document.getElementById(modalId).classList.add(isVisible);
  });
}

// FUNCION CERRAR MODAL
function closeModal() {
  document.querySelector(".modal").style.display = "none";
}

// CERRAR EN ESCAPE
document.addEventListener("keyup", (e) => {
  // if we press the ESC
  if (e.key == "Escape" && document.querySelector(".modal.is-visible")) {
    closeModal();
  }
});

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
