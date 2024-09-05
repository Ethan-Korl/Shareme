from django.urls import path
from accounts.views import *

app_name = "accounts"

# urlpatterns = []
urlpatterns = [
    # path("otp/", RequestOtpLogin.as_view(), name="register"),
    # path("verify-email/", VerifyEmailCode.as_view(), name="verify-email"),
    path("signup/", signup, name="signup"),
    path("login/", login, name="login"),
    path("auth/check-username/", check_username, name="check-username"),
    path("auth/<username>/", verify_otp, name="verify-otp"),
    # path("reset-password/", ResetPasswordChange.as_view()),
]
