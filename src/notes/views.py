from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
import logging
from .models import Note, Todo
from .forms import NoteCreateForm, TodoCreateForm
from json import dumps
from django.core import serializers

# Create your views here.

def note_list_view(request):
    notes = Note.objects.all()
    todos = Todo.objects.all()
    todoDataJSON = serializers.serialize('json', todos)
    note_form = NoteCreateForm()
    todo_form = TodoCreateForm()
    if request.method == 'POST':
        if 'deadline' not in request.POST:
            form = NoteCreateForm(request.POST)
            if form.is_valid():
                note = form.save(commit=False)
                note.save()
                return HttpResponseRedirect('/notes/')
        else:
            form = TodoCreateForm(request.POST)
            if form.is_valid():
                print('yes!')
                todo = form.save(commit=False)
                todo.save()
                return HttpResponseRedirect('/notes/')
            else: print('no!')
    else:
        note_form = NoteCreateForm()
        todo_form = TodoCreateForm()

    context = {
        'notes': notes,
        'note_form': note_form,
        'todo_form': todo_form,
        'dataJSON': todoDataJSON,
    }
    
    return render(request, 'notes/note_list.html', context)


def note_details_view(request, id):
    note = Note.objects.get(id=id)
    context = {
        'note': note
    }
    return render(request, 'notes/note_details.html', context)


def todo_details_view(request, id):
    todo = Todo.objects.get(id=id)
    context = {
        'todo': todo
    }
    return render(request, 'notes/todo_details.html', context)
