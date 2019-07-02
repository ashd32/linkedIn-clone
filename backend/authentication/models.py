from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from locations.models import Country, City
from .validations import UsernameValidator, validate_birthday


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(
            self, email, username,
            full_name, birthday, city,
            password, **extra_fields):

        if not email:
            raise ValueError("The given email must be set")
        if not username:
            raise ValueError("The given username must be set")
        if not full_name:
            raise ValueError("The given full name must be set")
        if not birthday:
            raise ValueError("The given birthday must be set")
        if not city:
            raise ValueError("The given city must be set")

        email = self.normalize_email(email)
        username = self.model.normalize_username(username)
        user = self.model(
            email=email,
            username=username,
            full_name=full_name,
            birthday=birthday,
            country=country,
            city=city
            ** extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, username, full_name, birthday,
                    city, password=None, **extra_fields):

        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(
            email, username, full_name, birthday, password, **extra_fields
        )

    def create_superuser(self, email, username, full_name, birthday, password,
                         **extra_fields):

        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(
            email, username, full_name, birthday, country, city, password,
            **extra_fields
        )


class User(AbstractBaseUser, PermissionsMixin):
    username_validators = UsernameValidator()

    username = models.CharField(
        db_index=True,
        max_length=50,
        unique=True,
        validators=[username_validators],
        error_messages={"unique": "A user with that username already exists"}
    )

    email = models.EmailField(db_index=True, unique=True)
    full_name = models.CharField(max_length=255)
    birthday = models.DateField(validators=[validate_birthday])
  
    city = models.ForeignKey(
        to=City, on_delete=models.SET_NULL,
        null=True, related_name="users"
    )
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "full_name", "birthday", ]

    def __str__(self):
        return self.username

    def get_short_name(self):
        return self.username

    def get_full_name(self):
        return self.full_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        send_mail(subject, message, from_email, [self.email], **kwargs)

    def get_location(self):
        return self.city.country, self.city