import random

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponseRedirect
from django.views.generic import CreateView, DetailView, TemplateView, ListView, DeleteView
from django.views.generic.edit import FormMixin

from eng.eng_forms import RegisterForm, AddNewWordForm, QuestionForm
from eng.models import EngUser, Words


class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'register.html'
    success_url = '/login/'


class Login(LoginView):
    template_name = 'login.html'

    def get_success_url(self):
        return f"/profile/{self.request.user.pk}/"


class Logout(LoginRequiredMixin, LogoutView):
    login_url = '/login/'
    next_page = '/login/'


class ProfileView(LoginRequiredMixin, DetailView):
    login_url = '/login/'
    model = EngUser
    template_name = 'profile.html'

    def get_context_data(self, **kwargs):
        kwargs = super().get_context_data()
        kwargs['all_words'] = Words.objects.filter(owner=self.request.user).count()
        kwargs['not_learned_words'] = Words.objects.filter(owner=self.request.user, status=False).count()
        return kwargs


class IndexView(TemplateView):
    template_name = "index.html"


class AddNewWordView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    form_class = AddNewWordForm
    template_name = 'add_word.html'

    def form_valid(self, form):
        word = form.save(commit=False)
        word.first = form.cleaned_data['first'].lower()
        word.second = form.cleaned_data['second'].lower()
        word.owner = self.request.user
        return super().form_valid(form=form)

    def get_success_url(self):
        return f'/profile/{self.request.user.pk}/'


class WordsListView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    template_name = 'words_list.html'
    paginate_by = 25

    def get_queryset(self):
        return Words.objects.filter(owner=self.request.user)


class DeleteWordView(LoginRequiredMixin, DeleteView):
    login_url = '/login/'
    model = Words


class PlayView(LoginRequiredMixin, FormMixin, DetailView):
    login_url = '/login/'
    template_name = 'play.html'
    form_class = QuestionForm

    def get_queryset(self):
        return Words.objects.filter(owner=self.request.user)

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        next_word = random.randint(0, self.get_queryset().count())
        question = form.cleaned_data['second']
        obj = self.get_object()
        if obj.second == question:
            obj.status = True
            obj.save()
        return HttpResponseRedirect(f'/word/play/{next_word}')


