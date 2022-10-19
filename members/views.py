from multiprocessing import context
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Members

import members
from .models import Members


def index(request):
    mymembers = Members.objects.all().values()
    temblate = loader.get_template('myfirst.html')
    context = {
        'mymembers': mymembers
    }
    return HttpResponse(temblate.render(context, request))


def add(request):
    temblate = loader.get_template('add.html')
    return HttpResponse(temblate.render({}, request))


def addrecord(request):
    x = request.POST['first']
    y = request.POST['last']
    member = Members(firstname=x, lastname=y)
    member.save()
    return HttpResponseRedirect(reverse('index'))


def deleterecord(request, id):
    member = Members.objects.get(id=id)
    member.delete()
    return HttpResponseRedirect(reverse('index'))


def update(request, id):
    mymember = Members.objects.get(id=id)
    template = loader.get_template('update.html')
    context = {
        'mymember': mymember,
    }
    return HttpResponse(template.render(context, request))


def updaterecord(request, id):
    member = Members.objects.get(id=id)
    x = request.POST['first']
    y = request.POST['last']
    member.firstname = x
    member.lastname = y
    member.save()
    return HttpResponseRedirect(reverse('index'))

# Create your views here.
