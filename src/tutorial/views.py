from django.shortcuts import render
from django.views.generic import ListView
from .models import Person
from .tables import PersonTable
from django_tables2 import RequestConfig

def people(request):
	table  = PersonTable(Person.objects.all())
	RequestConfig(request).configure(table)
	return render(request, 'tutorial/people.html', {'table': table})

    # return render(request, 'tutorial/people.html', {'people': Person.objects.all()})