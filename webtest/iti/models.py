from __future__ import unicode_literals

from django.db import models

from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible  # only if you need to support Python 2
class Transaction(models.Model):
    trans_id = models.IntegerField(primary_key=True, blank=True, null=False)
    time = models.DateField(blank=False, null=False, auto_now_add=True)
    email = models.TextField(blank=False, null=False)
    amount = models.TextField(blank=False, null=False)
    cashtype = models.TextField(blank=False, null=False)
    def __str__(self):
        return self.email
