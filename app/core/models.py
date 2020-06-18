from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager, \
                                        PermissionsMixin

# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self,email,password=None,**extra_fields):
        '''Creates and save a new user'''
        if not email:
            raise ValueError('Users must have an email Address')
        user = self.model(email=self.normalize_email(email),**extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_super_user(self,email,password):

        user = self.create_user(email,password)

        user.is_superuser = True
        user.is_staff = True

        user.save(using=self._db)
        return user

class User(AbstractBaseUser,PermissionsMixin):
    '''Custom user model that supports using email instead of Username'''
    email = models.EmailField(max_length = 255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
