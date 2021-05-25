from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

from eng.models import EngUser, Words


class RegisterForm(UserCreationForm):
    class Meta:
        model = EngUser
        fields = ['username']


class AddNewWordForm(ModelForm):
    class Meta:
        model = Words
        fields = ['first', 'second']


class QuestionForm(ModelForm):
    class Meta:
        model = Words
        fields = ['second']
