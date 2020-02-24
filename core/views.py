from django.shortcuts import render

from django.http import HttpResponse

import data


def index(request):
    notes = data.Notes
    breakpoint()
    # return HttpResponse("This is a text response, unrelated to the database.")
    #The notes below is a dictionary.
    return render(request, 'base.html', {'notes': notes})


# Create your views here.

