function openPopup(type) {
  document.getElementById('overlay-trab').classList.add('active');
  document.querySelectorAll('.popup-trab').forEach(popup => popup.classList.remove('active'));
  document.getElementById('popup-' + type).classList.add('active');
}

function closePopup() {
  document.getElementById('overlay-trab').classList.remove('active');
  document.querySelectorAll('.popup-trab').forEach(popup => popup.classList.remove('active'));
}

function toggleMenu(button) {
      button.classList.toggle('active');
      document.getElementById('sidebar').classList.toggle('active');
    }

    function toggleSubmenu(menuItem) {
      menuItem.classList.toggle('open');
    }