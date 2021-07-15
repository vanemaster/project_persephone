from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.uploadDatabase, name='upload'),
]