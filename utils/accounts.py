from utils.base import *


class GenerateOtp:
    def __init__(self, username, user_repo=CustomUserRepo) -> None:
        self.username = username
        self.user_repo = user_repo
        self.user = self.user_repo.get_user(self.username)

    @staticmethod
    def new_generate_and_hash_otp():
        otp = str(randint(10000, 99999))
        return otp

    def generate_and_hash_otp(self):
        otp = str(randint(10000, 99999))
        self.user.set_password(otp)
        return otp
