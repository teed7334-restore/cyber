# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from home.models import Slider, About, Management_Philosophy, Partner, Contact, Company
from django import forms
from cloudinary import api

# Create your views here.
def index(request):

    if True == do_post(request):
        return render(request, 'alert.html')

    response = {
        'homepage': homepage(),
        'about': about(),
        'management_philosophy': management_philosophy(),
        'partner': partner(),
        'company': company(),
    }
    return render(request, 'index.html', response)

def homepage():
    response = {
        'company_name': '聖森股份有限公司',
        'slider': Slider.objects.all()
    }
    return response;

def about():
    response = About.objects.all()[:1]
    return response

def management_philosophy():
    response = Management_Philosophy.objects.all()[:1]
    return response

def partner():
    response = Partner.objects.all()
    return response;

def company():
    response = Company.objects.all().order_by('pk')
    return response;

def do_post(request):
    if request.method == 'POST':
        form = Contact_Form(request.POST)
        if form.is_valid():
            form.save()
            return True

    return False

class Contact_Form(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ['name', 'email', 'url', 'message']
