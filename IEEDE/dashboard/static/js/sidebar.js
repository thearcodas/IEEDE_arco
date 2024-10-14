$(document).ready(function () {
  $("#barswitch").click(function () {
    $(".sidebar").toggleClass("sidebar-collapse");
    $(".main-body").toggleClass("expand");
    $("#logo").toggleClass("logoCollapse");
    $(".aspan").toggleClass("a-span");
    $(".side-a").toggleClass("sidea");
  });
});