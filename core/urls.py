from django.urls import path

from .views import *

urlpatterns = [
    path('', index),
    path('delete-music/', delete_track),
    path('add-music/', add_track),
]
