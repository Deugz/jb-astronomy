const button = document.getElementById("menu-toggle");

const toggle = () => {
  document.body.classList.toggle("menu-toggled");
}

button.onclick = () => toggle();

setTimeout(toggle, 200);