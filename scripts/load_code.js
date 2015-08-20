jQuery(document).ready(function() {

  $("div#expander").click(function() {
      var expander_max_height= $(this).parent().find("#code-holder").css("max-height");
      var replace_text = $(this).text();
      if (expander_max_height == "0px") {
        $(this).parent().find("#code-holder").css("max-height", $(this).parent().find("#code-holder")[0].scrollHeight);
        $(this).text(replace_text.replace(/Show/, "Hide"));
      } else {
        $(this).parent().find("#code-holder").css("max-height", "0px");
        $(this).text(replace_text.replace(/Hide/, "Show"));
      }
  });

  jQuery(".change-view").click(function() {
    var view = this.id;
    jQuery("#content").load("views/"+view+".html");
  });

  jQuery.each(document.getElementsByClassName("code"), function(index, value) {
    jQuery(value).find("#code-holder").load("resources/"+value.id+".txt");
  });
});
