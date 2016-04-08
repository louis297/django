

from django.db import models



class chartDefault(models.Model):
    id = models.IntegerField(primary_key=True, blank=True, null=False)
    name = models.TextField()
    value = models.FloatField()
    group = models.IntegerField()

    def __str__(self):
        return self.name
