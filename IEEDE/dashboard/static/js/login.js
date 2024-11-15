$(document).ready(function () {
    $('#logform').submit(function() { 
        var mec = $("#mec");
        var mecerror = $("#mecerror");
        var otp = $("#otp");
        var otperror = $("#otperror");
        var logtxt = $("#log-txt");
        if (mec.val() == "") {
          mec.css("borderColor", "#9B111E");
          mecerror.css("visibility", "visible");
          return false;
        } 
        else {
          $('#logform').css("display", "none");
          logtxt.html(
            "An OTP will be sent to your registered email shortly. Please do not refresh the page. Thank you!"
          );
          $('#logotpform').css("display","flex");
          $('#logotpform').submit(function () { 
             if (otp.val() == "") {
               otp.css("borderColor", "#9B111E");
               otperror.css("visibility", "visible");
               return false;
             }
          });
          return false;
        }
    });
    $('#inslogform').submit(function () { 
        if($('#lic').val()==""){
          $("#lic").css("borderColor", "#9B111E");
          $("#licerror").css("visibility", "visible");
          return false;
        }
        if ($("#psw").val() == "") {
          $("#psw").css("borderColor", "#9B111E");
          $("#pswerror").css("visibility", "visible");
          return false;
        }
      
    });
     $("#emplogform").submit(function () {
       if ($("#emp").val() == "") {
         $("#emp").css("borderColor", "#9B111E");
         $("#emperror").css("visibility", "visible");
         return false;
       }
       if ($("#epsw").val() == "") {
         $("#epsw").css("borderColor", "#9B111E");
         $("#epswerror").css("visibility", "visible");
         return false;
       }
     });

     $("#mobform").submit(function () { 
      if ($("#ph").val().length < 10) {
        $("#ph").css("borderColor", "#9B111E");
        $("#pherror").css("visibility", "visible");
        return false;
      }
      else{
          $("#mobform").css("display", "none");
          $("#for-txt").html(
            "An OTP has been sent to your phone. Enter it here and do not refresh the page."
          );
          $("#otpforform").css("display", "flex");
          $("#otpforform").submit(function () {
            if ($('#fotp').val() == "") {
              $("#fotp").css("borderColor", "#9B111E");
              $("#fotperror").css("visibility", "visible");
              return false;
            }
            else{
               $("#otpforform").css("display", "none");
            $("#for-txt").html(
            "Enter your password and confirm it in the fields provided. Ensure they match before proceeding."
          );
          $("#pswform").css("display", "flex");
          $("#pswform").submit(function () {
            if ($('#npsw').val().length < 6) {
              $("#npsw").css("borderColor", "#9B111E");
              $("#npswerror").css("visibility", "visible");
              return false;
            }
            if ($('#cpsw').val() != $('#npsw').val()) {
              $("#cpsw").css("borderColor", "#9B111E");
              $("#cpswerror").css("visibility", "visible");
              return false;
            }
            });
            return false;
          }
          });
          return false;
      }
      
     });
});