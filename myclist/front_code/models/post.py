from django.db import models
from models import UserModel
from model.geography import CityModel


class PostModel(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    city = models.ForeignKey(CityModel, on_delete=models.CASCADE)
    post_date = models.DateTimeField('post date', editable=False)
    modified_date = models.DateTimeField('modified date')
    activate = models.BooleanField(default=True)


class PictureModel(models.Model):
    post = models.ForeignKey(PostModel, on_delete=models.CASCADE)
    path = models.CharField(max_length=200)
    activate = models.BooleanField(default=True)

