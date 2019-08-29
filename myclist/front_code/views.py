from django.shortcuts import render
from django.http import HttpResponse

from .view.register import *

def index(request):
    return HttpResponse(encrypt_pass('abc'))

