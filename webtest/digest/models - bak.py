from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
import datetime

from django.utils import timezone

# Create your models here.
##from sqlobject import *
##import os.path
##
##dbfile = 'enzyme.db3'
##
### Magic formatting for database URI
##conn_str = os.path.abspath(dbfile)
##conn_str = 'sqlite:'+ conn_str
##
##sqlhub.processConnection = connectionForURI(conn_str)

##class enzyme_list(models.Model):
##    name = StringCol()
##    amount = IntCol()
##    digest = StringCol()
##    start_pos = StringCol()
##
##class enzymes():
##    enzyme = []
##    def __init__(self):
##        for e in enzyme_list.select():
##            self.enzyme.append((e.name,e.amount,e.digest,e.start_pos))
