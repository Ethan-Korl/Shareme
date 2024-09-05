from django.http import HttpRequest
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib import messages
from utils.general import SendEmail
from utils.accounts import GenerateOtp
from accounts.repository import *
from .utils import generate_code, extract_name


def signup(request: HttpRequest):
    user_repo = CustomUserRepo
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        if user_repo.get_user(username):
            return render(
                request,
                "components/messages/error_message.html",
                {"message": f"{username} already exists"},
            )
        else:
            generate_otp = GenerateOtp(username)
            user_repo.create_user(
                username=username,
                email=email,
                password=generate_otp.new_generate_and_hash_otp(),
            )
            send_email = SendEmail(
                user_email=email,
                template="emails/otp_email.html",
                subject="Your OTP Verification",
                context={},
            )
            return render(
                request,
                "components/accounts/otp_input.html",
                {
                    "message": f"OTP sent to {email}",
                    "email": f"{email}",
                },
            )

    return render(request, "front_end/signup.html")


def login(request: HttpRequest):
    user_repo = CustomUserRepo
    if request.method == "POST":
        username = request.POST.get("username")
        otp = request.POST.get("otp")
        user = user_repo.get_user(username)
        if user:
            generate_otp = GenerateOtp(username)
            mail = SendEmail(
                user_email=user.email,
                template="emails/otp_email.html",
                subject="Your OTP Auth",
                context={"otp": generate_otp.generate_and_hash_otp()},
            )
            mail.send_email()
            response = HttpResponse()
            response["HX-Redirect"] = reverse(
                "accounts:verify-otp", kwargs={"username": username}
            )
            messages.info(request, f"OTP has been sent to {user.email}")
            return response
            # return render(
            #     request,
            #     "components/accounts/otp_input.html",
            #     {"message": f"OTP has been sent to {user.email}"},
            # )
        else:
            return render(
                request,
                "components/messages/error_message.html",
                {"message": "user does not exists"},
            )
    return render(request, "front_end/login.html")


def verify_otp(request: HttpRequest, username):
    if request.method == "POST":
        otp = request.POST.get("otp")
        user = authenticate(request, username=username, password=otp)
        if user:
            login(request, user)
            response = HttpResponse()
            response["HX-Redirect"] = reverse("")
            return response
        else:
            return render(
                request,
                "components/messages/error_message.html",
                {"message": "Invalid username oR OTP"},
            )
    return render(request, "front_end/verify_otp.html", {"username": username})
