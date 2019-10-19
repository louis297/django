from django.db import models
from django.utils import timezone


class UserModel(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    NA = 'N'
    GENDER = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (NA, 'Not applied')
    )

    username = models.CharField(max_length=40)
    password_encrypt_version = models.IntegerField()
    password_iteration = models.IntegerField(default=1)
    password_salt = models.CharField(max_length=100)
    password_encrypted = models.CharField(max_length=256)
    email = models.CharField(max_length=100)
    birthday = models.DateField()
    gender = models.CharField(choices=GENDER, max_length=20, default=NA)
    register_date = models.DateTimeField('register date', editable=False)
    last_login_date = models.DateTimeField('last login date')
    last_login_ip = models.CharField(max_length=30)
    phone = models.CharField(max_length=20)

    activate = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.register_date:
            self.register_date = timezone.now()
