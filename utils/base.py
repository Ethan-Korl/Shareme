from cryptography.fernet import Fernet
from django.conf import settings
from django.contrib.auth.hashers import make_password
from random import randint
from accounts.repository import CustomUserRepo
