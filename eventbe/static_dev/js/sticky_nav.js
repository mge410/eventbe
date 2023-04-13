var sticky;
var header;

document.addEventListener("DOMContentLoaded", function () {
  // Get the header
  header = document.getElementById("navbar_id");

  // Get the offset position of the navbar
  sticky = header.offsetTop;
});

// When the user scrolls the page, execute myFunction
window.onscroll = function () {
  navBarFixing();
};

// Add the sticky class to the header when you reach its scroll position. Remove "sticky" when you leave the scroll position
function navBarFixing() {
  if (window.pageYOffset >= sticky + 220) {
    header.classList.add("sticky");
  } else {
    header.classList.remove("sticky");
  }
}
