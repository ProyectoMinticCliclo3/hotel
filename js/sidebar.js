// SIDEBAR
function openNav() {
  document.getElementById("mySidebar").style.width = "16rem";
  document.getElementById("main").style.marginLeft = "16rem";
}

function closeNav() {
  document.getElementById("mySidebar").style.width = "0";
  document.getElementById("main").style.marginLeft = "0";
}

var modal = document.getElementById("modal-id01");
window.onclick = function (event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
};
