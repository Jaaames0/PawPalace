from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


class Cat(models.Model):
    Cattitle = models.CharField('Заголовок', max_length=100, default="")
    Catdescriptionshort = models.CharField('Краткое описание', max_length=80, default="")
    Catname = models.CharField('Кличка', max_length=80, default="")
    Catdescription = models.TextField('Описание', max_length=8000, default="")
    Catpic = models.ImageField('Главное фото', upload_to='imgs/Cats/', default=0)
    Catplace = models.CharField('Город', max_length=200, default="")

    hostpic = models.ImageField('Фото приюта', upload_to='imgs/Cats/avatars/', default=0)
    hostname = models.CharField('Приют', max_length=100, default="")
    hostemail = models.EmailField('Почта приюта', max_length=100, default="")

    def __str__(self):
        return self.Cattitle

    def get_absolute_url(self):
        return reverse('main', kwargs={'pk': self.pk})


class Profile(models.Model):
    user = models.OneToOneField('main.NewUser', on_delete=models.CASCADE)
    mobileph = models.IntegerField()
    email = models.EmailField()
    lastname = models.CharField(max_length=100)
    firstname = models.CharField(max_length=100)

class NewUser(AbstractUser):
    email = models.EmailField(null=True)
    mobilephone = models.CharField('Номер',max_length=12,default='')
