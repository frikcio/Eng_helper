from django.urls import path

from eng.views import RegisterView, Login, AddNewWordView, ProfileView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', Login.as_view(), name='login'),
    path('profile/<int:pk>', ProfileView.as_view(), name='profile'),
    path('word/add/', AddNewWordView.as_view(), name='add_word'),
]
