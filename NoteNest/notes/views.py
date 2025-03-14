from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.db.models import Q
from .models import Note, Category
from .forms import NoteForm
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView as AuthCreateView

class NoteListView(LoginRequiredMixin, ListView):
    model = Note
    template_name = 'notes/note_list.html'
    context_object_name = 'notes'

    def get_queryset(self):
        queryset = Note.objects.filter(owner=self.request.user).order_by('-updated_at')
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(
                Q(title__icontains=query) | Q(content__icontains=query)
            )
        return queryset

class NoteDetailView(LoginRequiredMixin, DetailView):
    model = Note
    template_name = 'notes/note_detail.html'
    context_object_name = 'note'

    def get_queryset(self):
        return Note.objects.filter(owner=self.request.user)

class NoteCreateView(LoginRequiredMixin, CreateView):
    model = Note
    form_class = NoteForm
    template_name = 'notes/note_form.html'
    success_url = reverse_lazy('note_list')

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        # Show only global categories (owner is null) or categories created by this user
        form.fields['category'].queryset = Category.objects.filter(
            Q(owner__isnull=True) | Q(owner=self.request.user)
        )
        return form

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class NoteUpdateView(LoginRequiredMixin, UpdateView):
    model = Note
    form_class = NoteForm
    template_name = 'notes/note_form.html'
    success_url = reverse_lazy('note_list')

    def get_queryset(self):
        return Note.objects.filter(owner=self.request.user)

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['category'].queryset = Category.objects.filter(
            Q(owner__isnull=True) | Q(owner=self.request.user)
        )
        return form

class NoteDeleteView(LoginRequiredMixin, DeleteView):
    model = Note
    template_name = 'notes/note_confirm_delete.html'
    success_url = reverse_lazy('note_list')

    def get_queryset(self):
        return Note.objects.filter(owner=self.request.user)

# New: View to handle user registration (if not already present)
class SignUpView(AuthCreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')

# New: View for creating categories
class CategoryCreateView(LoginRequiredMixin, CreateView):
    model = Category
    fields = ['name']
    template_name = 'notes/category_form.html'
    success_url = reverse_lazy('note_list')

    def form_valid(self, form):
        # If the user is superuser/admin, create a global category (owner remains None)
        if not self.request.user.is_superuser:
            form.instance.owner = self.request.user
        # For superusers, owner stays null so the category is global.
        return super().form_valid(form)
