$(window).scroll(function() {
  if ($(document).scrollTop() > 50) {
    $('#nav').addClass('mini');
  } else {
    $('#nav').removeClass('mini');
  }
});