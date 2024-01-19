from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, username, full_name, phone_number, password=None, **extra_fields):
        if not username:
            raise ValueError("username must be set")
        if not full_name:
            raise ValueError("fullname must be set")
        if not phone_number:
            raise ValueError("phone number must be set")
        if not password:
            raise ValueError("password must be set")
        user = self.model(
            username=username,
            full_name=full_name,
            phone_number=phone_number
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, username, full_name, phone_number, password, **extra_fields):
        user = self.create_user(
            username=username,
            full_name=full_name,
            phone_number=phone_number,
            password=password,
            **extra_fields
        )
        user.is_active = True
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    username = models.CharField(max_length=20, blank=False, null=False, primary_key=True)
    full_name = models.CharField(max_length=20, null=False)
    phone_number = models.CharField(max_length=20, unique=True, blank=False)
    profile_picture = models.ImageField(null=True, blank=True)
    bio = models.TextField(blank=True, null=True)
    password = models.CharField(max_length=20)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = [ 'full_name', 'phone_number', 'password']  #this fields used when creating a super user through command line

    def __str__(self):
        return self.username
    
    def has_perm(self, perm, obj=None):
        return True
    def has_module_perms(self, app_label):
        return True
    

