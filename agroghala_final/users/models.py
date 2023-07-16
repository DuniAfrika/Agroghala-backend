from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager



class CustomUserManager(BaseUserManager):
    def create_superuser(self, first_name, last_name, email, address, password, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('password', password)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                f'Superuser must be assigned to is_staff=True'
            )
        
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                f'Superuser must be assigned to is_superuser=True'
            )
        
        return self.create_user(first_name, last_name, email, address, password, **other_fields)
    
    def create_user(
            self, first_name, last_name,
            email, phone_number, address,
            password, **other_fields
            ):

        other_fields.setdefault('is_farmer', True)
        other_fields.setdefault('is_active', True)
        
        if not email:
            raise ValueError(f'Email Field is Required')
        
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number,
            address=address,
            **other_fields
        )
        user.set_password(password)
        user.save()
        
        return user


class NewUser(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(blank=False, max_length=255)
    last_name = models.CharField(blank=False, max_length=255)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=10)
    address = models.CharField(max_length=255)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_farmer = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'address']
    def __str__(self):
        return (self.first_name + " " + self.last_name)


