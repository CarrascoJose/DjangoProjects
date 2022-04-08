from django.urls import path
from .views import HomePageView,NoteView, AddNoteView,DeleteNoteView

urlpatterns = [
    path('home/',HomePageView.as_view(),name="home"),
    path('note/<int:pk>/',NoteView.as_view(),name="note"),
    path('add_note/',AddNoteView.as_view(),name="add_note"),
    path('delete/<int:pk>/',DeleteNoteView.as_view(),name="delete_note"),
]