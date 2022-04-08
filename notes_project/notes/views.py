from django.shortcuts import render
from django.views.generic import TemplateView, CreateView,ListView, DeleteView
from .models import AppUser,Note
from django.urls import reverse_lazy
from .forms import NoteForm

# Create your views here.

class HomePageView(ListView):
    model = Note
    template_name = 'notes/home.html'




class NoteView(TemplateView):
    model = Note
    template_name = 'notes/note.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['note'] = self.model.objects.get(pk=self.kwargs['pk'])
        return context


class AddNoteView(CreateView):
    model = Note
    template_name = 'notes/add_note.html'
    form_class = NoteForm
    success_url = reverse_lazy('home')


class DeleteNoteView(DeleteView):
    model = Note
    template_name = 'notes/delete_note.html'
    success_url = reverse_lazy('home')


        