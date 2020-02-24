from django.shortcuts import render

from django.http import HttpResponse

import data


def index(request):
    notes = data.NOTES
    #The notes below is a dictionary.
    return render(request, 'base.html', {'notes': notes})


# Create your views here.

