# -*- coding: utf-8 -*-
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.template import loader
from django.core.urlresolvers import reverse
from django.views import generic

from .models import Transaction
import time

####################
#currency symbols
#also the supported types of currency in /send
#can be saved in database instead
currency_symbol = {'USD':u'$', 'EUR':u'€', 'JPY':u'¥', 'CNY':u'¥'}
####################


def index(request):
    template = loader.get_template('iti/index.html')
    context = {}
    return HttpResponse(template.render(context, request))

def send(request):
    template = loader.get_template('iti/send.html')
    currency_list = currency_symbol.keys()
    currency_list.sort(reverse=True)
    context = {'currency': currency_list}
    return HttpResponse(template.render(context, request))

def success(request):
    #time.sleep(5)
    template = loader.get_template('iti/success.html')
    try:
        transaction = Transaction(email=request.POST['email'],
                                  amount=request.POST['amount'],
                                  cashtype=request.POST['cashtype'])
        transaction.save()
    except:
        return HttpResponseRedirect('/iti/fail')
    print request.POST['cashtype']
    print transaction.amount
    context = {}
    context['amount'] = request.POST['amount']
    context['email'] = request.POST['email']
    return HttpResponse(template.render(context, request))

def fail(request):
    template = loader.get_template('iti/fail.html')
    context = {}
    return HttpResponse(template.render(context, request))

def history(request):
    transactions = Transaction.objects.all()
    tr_history = []
    for i in transactions:
        t=currency_symbol[i.cashtype]
        t += i.amount
        tr_history.append((i.time,i.email,t,i.trans_id))
    template = loader.get_template('iti/history.html')
    context = {'trans' : tr_history}
    return HttpResponse(template.render(context, request))

def transaction(request, pk):
    trans = get_object_or_404(Transaction, trans_id=pk)
    template = loader.get_template('iti/transaction.html')
    context = {}
    t=currency_symbol[trans.cashtype] 
    context['amount'] = t+trans.amount
    context['email'] = trans.email
    context['date'] = trans.time
    context['trans_id'] = pk
    print trans.time
    return HttpResponse(template.render(context, request))

def del_trans(request, pk):
    trans = get_object_or_404(Transaction, trans_id=pk)
    try:
        trans.delete()
    except:
        return HttpResponseRedirect('/iti/fail')
    template = loader.get_template('iti/del_success.html')
    context = {}
    return HttpResponse(template.render(context, request))
