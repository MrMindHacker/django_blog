from django.contrib import admin
from django.urls import path
from .views import photo_list, ImageDetailView
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', photo_list, name = 'photo_list' ),
    path('/view/<int:pk>', ImageDetailView.as_view(), name='photo'),
]