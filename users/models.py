from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import (
    BaseUserManager,
    AbstractBaseUser,
    PermissionsMixin,
    Group,
)
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import Permission


class CustomUserPermissions(Permission):
    class Meta:
        permissions = [
            ("is_head_technician", "Is Head Technician"),
            ("can_view_profit", "Can View Profit"),
        ]

# Create your models here.
class UserManager(BaseUserManager):
    """Class to manage the creation of user objects"""
    def create_user(self, username, email, password=None):
        """Creates and returns a user object
        Arguments:
        username: the string to use as username
        email: the string to use as email
        password: the string to use as password

        Optionals:
        is_staff: Boolean to indicate a user is staff or not
        is_admin: Boolean to indicate a user is an admin or not
        is_active: Boolean to indicate a user can login or not

        Return:
            A user object
        """
        if not username:
            raise ValueError('Users must have a username')

        if not email:
            raise ValueError('Users must have an email address')

        if not password:
            raise ValueError('Users must have a password')

        user = self.model(username=username,email = self.normalize_email(email),)
        user.set_password(password)
        user.is_active=True
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password):
        """Creates an admin user object
        Arguments:
        username: the string to use as username
        email: the string to use as email
        password: the string to use as password

        Return:
            A user object
        """
        user = self.create_user(username, email, password=password)
        user.is_admin=True
        user.is_superuser=True
        user.save(using=self._db)
        return user



class User(AbstractBaseUser, PermissionsMixin):
    class Genders(models.TextChoices):
        MALE = "M", "Male"
        FEMALE = "F", "Female"
    
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(verbose_name='email address', max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # user_data = models.OneToOneField('UserData', on_delete=models.SET_NULL, blank=True, null=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = UserManager()

    def __str__(self):
        return self.username

    def delete(self, using=None, keep_parents=False):
        self.is_active ^= True
        self.save()

    def get_full_name(self):
        full_name = "%s %s" % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        return self.first_name

    def getUrl(self):
        return reverse_lazy('accounts:detail', kwargs={'pk':self.pk})
    
    def email_user(self, subject, message, from_email=None, **kwargs):
        """Send an email to this user."""
        send_mail(subject, message, from_email, [self.email], **kwargs)

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.is_admin

class UserData(models.Model):
    first_name = models.CharField(max_length=150, blank=True, null=True)
    last_name = models.CharField(max_length=150, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='pps/', default='default-profile.jpg')
    # gender = models.