from django.urls import path

from eng.views import *

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('profile/<int:pk>/', ProfileView.as_view(), name='profile'),
    path('word/add/', AddNewWordView.as_view(), name='add_word'),
    path('word/delete/<int:pk>/', DeleteWordView.as_view(), name='delete_word'),
    path('word/list/', WordsListView.as_view(), name='words_list'),
    path('word/play/<int:pk>/', PlayView.as_view(), name='play'),
]
