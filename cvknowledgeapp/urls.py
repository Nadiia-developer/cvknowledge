from django.urls import path
from . import views

urlpatterns = [
    path('registration/', views.registration, name='registration'),
    path('theory/', views.theoretical_knowledge, name="theoretical_knowledge"),
]