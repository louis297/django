from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible



@python_2_unicode_compatible  # only if you need to support Python 2
class chartDefault:
    id = models.IntegerField(primary_key=True, blank=True, null=False)
    name = models.TextField()
    value = models.FloatField()
    group = models.IntegerField()
    def __str__(self):
        return self.name
