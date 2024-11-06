from django.core.mail import send_mail
from IEEDE.settings import EMAIL_HOST_USER

## send the otp to the user email
def OTP_mail(auto_generate_otp,email):
    send_mail(
            subject="Your OTP : ",
            message=f" {auto_generate_otp} \n\n\n Please don't share with anyone . ",
            from_email=EMAIL_HOST_USER,
            recipient_list=[email],
            fail_silently=False
            )
    