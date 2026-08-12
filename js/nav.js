document.addEventListener('DOMContentLoaded', function () {
  var placeholder = document.getElementById('topnav-placeholder');
  if (!placeholder) return;

  fetch('nav.html')
    .then(function (response) { return response.text(); })
    .then(function (html) {
      placeholder.outerHTML = html;

      var currentPage = window.location.pathname.split('/').pop();
      document.querySelectorAll('.topnav a').forEach(function (link) {
        if (link.getAttribute('href') === currentPage) {
          link.classList.add('active');
        }
      });
    });
});
