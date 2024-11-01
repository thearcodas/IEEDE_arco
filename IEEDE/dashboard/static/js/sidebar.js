$(document).ready(function () {
  $("#barswitch").click(function () {
    $(".sidebar").toggleClass("sidebar-collapse");
    $(".main-body").toggleClass("expand");
    $("#logo").toggleClass("logoCollapse");
    $(".aspan").toggleClass("a-span");
    $(".side-a").toggleClass("sidea");
  });
  function checkWidth() {
    if ($(window).width() < 480) {
      $("#barswitch").click(function () {
        $(".sidebar").toggleClass("mobile-side-expand");
        $(".sidebar").removeClass("sidebar-collapse");
        $(".main-body").removeClass("expand");
        $("#logo").removeClass("logoCollapse");
        $(".aspan").removeClass("a-span");
        $(".side-a").removeClass("sidea");
      });
      $(document)
        .off("click", "#close-bar")
        .on("click", "#close-bar", function () {
          $(".sidebar").removeClass("mobile-side-expand");
        });
    }
  }
  checkWidth();
  $(window).resize(checkWidth);

   let wasBelow480 = $(window).width() < 480;

   $(window).resize(function () {
     const isBelow480 = $(window).width() < 480;

     // Check if the screen width has crossed the 480px threshold in either direction
     if (wasBelow480 !== isBelow480) {
       location.reload();
     }

     // Update the tracking variable for future checks
     wasBelow480 = isBelow480;
   });
});