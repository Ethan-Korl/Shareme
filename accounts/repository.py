from accounts.models import CustomUser


class CustomUserRepo:
    model = CustomUser
    not_found = CustomUser.DoesNotExist

    @classmethod
    def get_user(cls, username: str):
        try:
            user = cls.model.objects.get(username=username)
        except cls.not_found:
            return None
        else:
            return user

    @classmethod
    def create_user(cls, username, email, password):
        user = cls.model.objects.create_user(
            username=username, email=email, password=username
        )
        user.save()
        return user
