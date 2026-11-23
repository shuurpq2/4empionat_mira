from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, email: str, password: str, **extra_fields):
        if not email:
            raise ValueError("Необходимо указать почту")

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email: str, password: str, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        return self.create_user(email, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField("Электронная почта", unique=True)
    is_active = models.BooleanField("Активен", default=True)
    is_staff = models.BooleanField("Является персоналом", default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []