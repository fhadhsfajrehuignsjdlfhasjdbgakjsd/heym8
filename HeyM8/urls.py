"""HeyM8 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('', lambda req:redirect('feed:feed', section='tan') if req.user.is_authenticated else redirect('/users/signin')),
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('communities/', include('communities.urls')),
    path('feed/', include('feed.urls')),
    path('complaint/', include('complaint.urls')),
    path('meetmate/', include('MeetMate.urls')),
    path('ratemate/', include('RateMate.urls')),
    path('chats/', include('chat.urls'))
]
