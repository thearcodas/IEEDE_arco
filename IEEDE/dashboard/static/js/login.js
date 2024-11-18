$(document).ready(function () {
  document
    .querySelector("#logform")
    .addEventListener("submit", async function (event) {
      event.preventDefault(); // Prevent default form submission

      const mecInput = document.querySelector("#mec");
      const mecError = document.querySelector("#mecerror");
      const logText = document.querySelector("#log-txt");
      const otpForm = document.querySelector("#logotpform");

      if (mecInput.value.trim() === "") {
        mecInput.style.borderColor = "#9B111E";
        mecError.style.visibility = "visible";
        return;
      } else {
        mecInput.style.borderColor = "";
        mecError.style.visibility = "hidden";
      }

      try {
        const response = await fetch("send-otp/", {
          
          method: "POST",
          headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": document.querySelector("[name=csrfmiddlewaretoken]").value,
          },
          body: JSON.stringify({ mec: mecInput.value.trim() }),
        });

        const data = await response.json();
        
        if (response.ok) {
          const mecId = data.mec_id;
          document.querySelector("#mec_id").value=mecId;
          logText.textContent =
            "An OTP has been sent to your registered email. Please do not refresh the page. Thank you!";
          logText.style.color = "green";
          document.querySelector("#logform").style.display="none";
          otpForm.style.display="flex";
        } else {
          console.error("Error sending OTP:", response.statusText);
          logText.textContent = "Error sending OTP or Enter valid MEC ID. Please try again.";
          logText.style.color = "red";
        }
      } catch (error) {
        console.error("Error:", error);
        logText.textContent = "Network error. Please try again.";
        logText.style.color = "red";
      }
    });

  document
    .querySelector("#logotpform")
    .addEventListener("submit", async function (event) {
      event.preventDefault(); // Prevent default form submission

      const mecIDInput = document.querySelector("#mec_id");
      const otpInput = document.querySelector("#otp");
      const otpError = document.querySelector("#otperror");

      if (otpInput.value.trim() === "") {
        otpInput.style.borderColor = "#9B111E";
        otpError.style.visibility = "visible";
        return;
      } else {
        otpInput.style.borderColor = "";
        otpError.style.visibility = "hidden";
      }

      try {
        let request_body = { otp: otpInput.value.trim(), 
          mec: mecIDInput.value.trim()
        };
        console.log(request_body);
        const response = await fetch("verify-otp/", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": "{{ csrf_token }}",
          },
          body: JSON.stringify(request_body),
        });

        if (response.ok) {
          alert("OTP Verified Successfully!");
          window.location.href = "/";
        } else {
          otpError.textContent = "Invalid OTP. Please try again.";
          otpError.style.visibility = "visible";
        }
      } catch (error) {
        alert(error);
        otpError.textContent = "Network error. Please try again.";
        otpError.style.visibility = "visible";
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
  $.ajax({
    url: 'institution-login/', // URL of the Django view
    method: 'POST',
    data: {
      lic: lic,
      psw: psw,
      csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
    },
    success: function (response) {
      if (response.status === "success") {
        alert("Login successful!");
        // Optionally redirect to another page
        window.location.href = "institution/";
      } else {
        alert("Login failed: " + response.error);
      }
    },
    error: function (xhr, status, error) {
      console.error("An error occurred: ", error);
      alert("An unexpected error occurred. Please try again.");
    },
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
    // if ($("#ph") < 10) {
    //   $("#ph").css("borderColor", "#9B111E");
    //   $("#pherror").css("visibility", "visible");
    //   return false;
    // }
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
    
   });
});