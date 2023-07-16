from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class UserProfileManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        
        user = self.model(email=self.normalize_email(email),
                username=username,
        )
        
        user.set_password(password)
        user.save(using=self._db)
        
        return user
    
    def create_superuser(self, email, username, password=None):
     user = self.create_user(email,
            password=password,
            username=username
     )
     
     user.is_staff = True
     user.is_admin = True
     user.is_superuser = True
     user.username = username
     user.save(using=self._db)
     
     return user

class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=16, unique=True)
    password = models.CharField(max_length=32)
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = UserProfileManager()

    

# class ChangePassword(models.Model):
#     old_password = models.CharField(max_length=32)
#     new_password = models.CharField(max_length=32)