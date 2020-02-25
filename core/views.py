from django.shortcuts import render

from django.http import HttpResponse

import data

# We are learning function based views. Not using class based views yet.
def  notes_list(request):
    notes = data.NOTES
    #The notes below is a dictionary.
    return render(request, 'core/notes_list.html', {'notes': notes})

def notes_detail(request, pk):
    note = data.NOTES[str(pk)]
    return render(request, 'core/notes_detail.html', {'note': note})



# Create your views here.

