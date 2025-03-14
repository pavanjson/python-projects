from django.urls import path
from .views import (
    NoteListView, NoteDetailView, NoteCreateView,
    NoteUpdateView, NoteDeleteView, CategoryCreateView
)

urlpatterns = [
    path('', NoteListView.as_view(), name='note_list'),
    path('note/<int:pk>/', NoteDetailView.as_view(), name='note_detail'),
    path('note/create/', NoteCreateView.as_view(), name='note_create'),
    path('note/<int:pk>/edit/', NoteUpdateView.as_view(), name='note_update'),
    path('note/<int:pk>/delete/', NoteDeleteView.as_view(), name='note_delete'),
    path('category/create/', CategoryCreateView.as_view(), name='category_create'),
]
