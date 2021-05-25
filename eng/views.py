from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView, DetailView

from eng.eng_forms import RegisterForm, AddNewWordForm
from eng.models import EngUser


class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'register.html'
    success_url = '/login/'


class Login(LoginView):
    template_name = 'login.html'

    def get_success_url(self):
        return f"/profile/{self.request.id}/"


class Logout(LoginRequiredMixin, LogoutView):
    login_url = '/login/'
    next_page = '/login/'


class AddNewWordView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    form_class = AddNewWordForm
    template_name = 'add_word.html'


class ProfileView(LoginRequiredMixin, DetailView):
    login_url = '/login/'
    model = EngUser
    template_name = 'profile.html'

