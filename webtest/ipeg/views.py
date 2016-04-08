from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.template import loader
from django.core.urlresolvers import reverse
from django.views import generic



def index(request):





    #loading template and construct page
    template = loader.get_template('ipeg/index.html')

    context = {
    }
    return HttpResponse(template.render(context, request))


def roi(request):
    template = loader.get_template('ipeg/roi.html')
    context = {

    }
    return HttpResponse(template.render(context, request))
