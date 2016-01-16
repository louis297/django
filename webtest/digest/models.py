# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible  # only if you need to support Python 2
class EnzymeList(models.Model):
    id = models.IntegerField(primary_key=True, blank=True, null=False)  # AutoField?
    name = models.TextField(blank=True, null=True)  # This field type is a guess.
    amount = models.TextField(blank=True, null=True)  # This field type is a guess.
    digest = models.TextField(blank=True, null=True)  # This field type is a guess.
    start_pos = models.TextField(blank=True, null=True)  # This field type is a guess.
    def __str__(self):
        return self.name
    class Meta:
        managed = False
        db_table = 'enzyme_list'
