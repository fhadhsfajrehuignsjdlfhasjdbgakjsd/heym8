from django.urls import path
from django.shortcuts import redirect
from . import views

app_name = 'feed'
urlpatterns = [
    path('<str:section>', views.feed, name='feed'),
    path('', lambda req:redirect('feed:feed', 'tan'))
]
