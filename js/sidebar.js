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
  document.getElementById("mySidebar").style.width = "16rem";
  document.getElementById("main").style.marginLeft = "16rem";
}

function closeNav() {
  document.getElementById("mySidebar").style.width = "5rem";
  document.getElementById("main").style.marginLeft = "5rem";
}

var modal = document.getElementById("modal-id01");
window.onclick = function (event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
};
