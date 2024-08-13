from os import name
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView
from .views import RequestOtpLogin , SignUpView

# urlpatterns = []
urlpatterns = [
    path("otp/", RequestOtpLogin.as_view(), name="register"),
    # path("verify-email/", VerifyEmailCode.as_view(), name="verify-email"),
    path("signup/",SignUpView.as_view(),name="signup"),
    path("login/", TokenObtainPairView.as_view(), name="obtaine-token"),
    # path("reset-password/", ResetPasswordChange.as_view()),
] 
