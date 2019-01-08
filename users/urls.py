from django.urls import path
from . import views

app_name="users"
urlpatterns = [
    path('signin', views.SignInAndUp, name="signInAndUp"),
    path('logout', views.Logout, name="logout"),
    path('intro', views.Intro, name="intro"),
    path('albums/<str:albumID>', views.AlbumPictures, name="albumPictures"),
    path('user/<str:uniqueURL>', views.UserPage, name="userPage"),
    path('settings/<str:section>', views.Settings, name='settings'),
    path('editStatus', views.EditStatus, name='editStatus'),
    path('newThought', views.NewThought, name='newThought'),

    path('confirm/<uuid:confirmationKey>', views.ConfirmEmail),
]
