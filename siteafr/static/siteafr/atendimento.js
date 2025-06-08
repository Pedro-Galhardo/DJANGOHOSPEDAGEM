function openPopup(type) {
      document.getElementById('overlay').classList.add('active');
      document.getElementById('popup-' + type).classList.add('active');
    }

    function closePopup() {
      document.getElementById('overlay').classList.remove('active');
      document.querySelectorAll('.popup').forEach(popup => popup.classList.remove('active'));
    }
function toggleMenu(button) {
      button.classList.toggle('active');
      document.getElementById('sidebar').classList.toggle('active');
    }

    function toggleSubmenu(menuItem) {
      menuItem.classList.toggle('open');
    }