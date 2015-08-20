var header_height = 48;
var sidebar_hidden = false;

$(document).ready(function(){
  $("header").css("height", header_height);
  $("#wrapper").css("top", header_height);
  $(".ext-link").css("top", (header_height-30)/2);

  $("#return-top").click(function() {
    window.scrollTo(0, 0);
  });
  jQuery("#wrapper").load("views/landing.html");
});


$(window).scroll(function() {
  var scrolled = $(window).scrollTop();
  var side_scrolled = $(window).scrollLeft();
  $("#sidebar").css("left", -side_scrolled);
  if (sidebar_hidden) {
    $("#hide-sidebar").css("left", -side_scrolled);
  } else {
    $("#hide-sidebar").css("left", -side_scrolled+176);
  }
  if (scrolled > header_height) {
    $("#return-top").css("display", "block");
    $("#sidebar").css("top", 0);
    $("#hide-sidebar").css("top", 0);
  } else {
    $("#return-top").css("display", "none");
    $("#sidebar").css("top", header_height-scrolled);
    $("#hide-sidebar").css("top", header_height-scrolled);
  }

});
