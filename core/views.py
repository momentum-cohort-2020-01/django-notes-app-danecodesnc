from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

from .models import Note
from .forms import NoteForm


def  notes_list(request):
    notes = Note.objects.all()
    return render(request, 'core/notes_list.html', {'notes': notes})

def notes_detail(request, pk):
    note = Note.objects.get(pk=pk)
    return render(request, 'core/notes_detail.html', {'note': note, 'pk': pk})


def notes_new(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save()
            return redirect('notes_detail', pk=note.pk)
    
    else:
        form = NoteForm()


    return render(request, 'core/notes_new.html', {'form': form})

def notes_edit(request, pk): 
    note = get_object_or_404(Note, pk=pk)
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('notes_detial', pk=note.pk)

    else:
        form = NoteForm(instance=note)

    return render(request, 'core/notes_edit.html', {"form": form})


    




















#  if request.method == "POST":
#         form = NoteForm(request.NOTE)
#         if form.is_valid():
#             note = note.save(commit=False)
#             note.author = request.user
#             note.published_date = timezone.now()
#             note.save()
#             return redirect('note_detail', pk=note.pk)
#     else:
#         form = NoteForm()
#     return render(request, 'core/note_detail.html', {'form': form})


#     def note_edit(request, pk):
#         note = get_object_or_404(Note, pk=pk)
#     if request.method == "POST":
#         form = NoteForm(request.NOTE, instance=note)
#         if form.is_valid():
#             note = form.save(commit=False)
#             note.author = request.user
#             note.published_date = timezone.now()
#             note.save()
#             return redirect('note_detail', pk=note.pk)
#     else:
#         form = NoteForm(instance=note)
#     return render(request, 'core/note_detail.html', {'form': form})
   