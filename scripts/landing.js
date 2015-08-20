$(document).ready(function() {
  jQuery.each($(document).find(".drop-down"), function(index, value) {
    value.style.maxHeight = String(0)+"px";
  });

  $("#sidebar").css("top", header_height);
  $("#hide-sidebar").css("top", header_height);

  $("#hide-sidebar").click(function() {
    if (sidebar_hidden) {
      sidebar_hidden = false;
      $("#sidebar").css("left", 0);
      $("#hide-sidebar").css("left", 176);
      $("#hide-sidebar").text("< < <");
      $("#content").css("left", 192);
      $("#content").css("min-width", 320);
    } else {
      sidebar_hidden = true;
      $("#sidebar").css("left", -176);
      $("#hide-sidebar").css("left", 0);
      $("#hide-sidebar").text("> > >");
      $("#content").css("left", 16);
      $("#content").css("min-width", 320+176);
    }
  });

  $("div.expand-drop-down").click(function() {
    if (jQuery(this).attr("id") == "collapsed") {
      jQuery(this).attr("id", "expanded");
      $(this).parent().css("max-height", String($(this).parent()[0].scrollHeight)+"px");
    } else {
      jQuery(this).attr("id", "collapsed");
      $(this).parent().css("max-height", String($(this)[0].scrollHeight+4)+"px");
    }
  });

  $("div.change-content").click(function() {
    var view = this.id;
    jQuery("#content").load("views/"+view+".html");
  });

  jQuery("#content").load("views/getting_started.html");

  jQuery.each($(document).find(".drop-down"), function(index, value) {
    value.style.maxHeight = String(value.childNodes[1].scrollHeight+4)+"px";
  });
});