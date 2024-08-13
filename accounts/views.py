from django.db.models.fields import generated
from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from django.contrib import auth
from rest_framework.settings import api_settings
from django.contrib.auth.models import update_last_login
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from django.conf import settings
from django.template.loader import render_to_string
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import EmailMessage
from .models import CustomUser, EmailVerificationCode
from .utils import generate_code, extract_name
# Create your views here.


class RequestOtpLogin(CreateAPIView):


    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user_email = serializer.validated_data.get("email")

            if not CustomUser.objects.filter(email=user_email).exists():
                return Response(data={"detail":"This user does not exists"}, status=status.HTTP_404_NOT_FOUND)   
                
            generated_password = str(generate_code()) 
            user = CustomUser.objects.get(email=user_email)
            user.set_password(generated_password)
            user.save()
            
            username = extract_name(user_email)
            email_body = render_to_string("otp.html", 
                                          context={
                                          "otp":generated_password,
                                          "username":username,
                                                   }
                                          )
            email = EmailMessage(
                    subject="ByteBridge Account OTP Verification",
                    body=email_body,
                    from_email=settings.EMAIL_HOST_USER,
                    to=[user_email],
                    )
            
            email.content_subtype = "html"
            email.send(fail_silently=True)
        
            return Response(data={"detail":"Your OTP has been sent to your email"}, status=status.HTTP_200_OK)   

# class RequestEmailCodeView(CreateAPIView):
#     email_verification_code = EmailVerificationCode.objects
#     serializer_class = SendEmailVerificationSerializer

#     def post(self, request, *args, **kwargs):
#         serializer = self.serializer_class(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             user_email = serializer.validated_data.get("email")

#             if not CustomUser.objects.filter(email=user_email).exists():
#                 return Response(data={"detail":"This user does not exists"}, status=status.HTTP_404_NOT_FOUND)   
#             generated_code = generate_code()            
#             generated_code = generate_code() 
          
#             self.email_verification_code.create(email=user_email, code=generated_code).save()
#             return Response(data={"detail":"Verification code has been sent to your email"}, status=status.HTTP_200_OK)   


# class VerifyEmailCode(CreateAPIView):
#     serializer_class = VerifyEmailCodeSerializer
#     code_store = EmailVerificationCode

#     def post(self, request, *args, **kwargs):
#         serializer = self.serializer_class(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             email = serializer.validated_data.get('email')
#             code = serializer.validated_data.get("code")
#             if self.code_store.objects.filter(email=email, code=code).exists():
#                 self.code_store.objects.get(email=email).delete()
#                 return Response(data={"detail":"Email Verified"},status=status.HTTP_200_OK)
#             else:
#                 return Response(data={"detail":"Code is invalid"},status=status.HTTP_400_BAD_REQUEST)


class SignUpView(CreateAPIView):
    serializer_class = SignUpSerializer
    user_model = CustomUser.objects

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if self.user_model.filter(email=request.data['email']).exists():
            return Response(data={"detail":"Email Already Registered",},
                                  status=status.HTTP_200_OK
                                  )
        if serializer.is_valid(raise_exception=True):
            email = serializer.validated_data['email']
            username = extract_name(email=email)
            otp_password = str(generate_code())
            user = self.user_model.create_user(username=username, email=email, password=otp_password)
            user.save()

            email_body = render_to_string("verification_email.html", 
                                          context={
                                          "username":username,
                                                   }
                                          )
            email = EmailMessage(
                    subject="ByteBridge Account Created Successfully",
                    body=email_body,
                    from_email=settings.EMAIL_HOST_USER,
                    to=[request.data['email']],
                    )
            email.content_subtype = "html"
            email.send(fail_silently=True)

            return Response(data={"detail":"Account Created Successfully Proceed To Login",},
                                  status=status.HTTP_200_OK
                                  )
        return Response(data={"detail":"User Creation Failed"}, status=status.HTTP_400_BAD_REQUEST)
