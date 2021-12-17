from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, User, UserManager
from django.db import models


class User(AbstractBaseUser, PermissionsMixin):
    is_ = (
        ('E', 'Employee'),
        ('M', 'Manager')
    )
    username = models.CharField(max_length=50, unique=True, db_index=True)
    email = models.EmailField(max_length=50, unique=True, db_index=True)
    profession = models.CharField(choices=is_, max_length=10, blank=False, null=False)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def __str__(self):
        return f'{self.username} | {self.profession}'

    class Meta:
        ordering = ['id']


class UserProfile(models.Model):
    GENDER = (
        ('M', 'Male'),
        ('F', 'Female')
    )

    image = models.FileField(upload_to='profile_img/', blank=True, null=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    about = models.TextField()
    birthday = models.DateField(auto_now_add=False)
    gender = models.CharField(choices=GENDER, max_length=100)
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{User.username}:{self.first_name} {self.last_name}.\n'

    class Meta:
        ordering = ['id']
