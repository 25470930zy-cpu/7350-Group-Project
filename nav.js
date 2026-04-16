document.addEventListener('DOMContentLoaded', function () {
  var groups = document.querySelectorAll('.nav-group');
  if (!groups.length) return;

  function closeAll() {
    groups.forEach(function (group) {
      group.classList.remove('submenu-open');
      var toggle = group.querySelector('.nav-toggle');
      if (toggle) toggle.setAttribute('aria-expanded', 'false');
    });
  }

  groups.forEach(function (group) {
    var toggle = group.querySelector('.nav-toggle');
    if (!toggle) return;

    toggle.addEventListener('click', function (event) {
      event.preventDefault();
      event.stopPropagation();
      var open = group.classList.toggle('submenu-open');
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    });

    var submenuLinks = group.querySelectorAll('.submenu a');
    submenuLinks.forEach(function (link) {
      link.addEventListener('click', function (event) {
        event.stopPropagation();
        closeAll();
        // let the link navigate normally
      });
    });
  });

  document.addEventListener('click', function (event) {
    if (!event.target.closest('.nav-group')) {
      closeAll();
    }
  });
});
