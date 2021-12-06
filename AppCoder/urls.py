from django.urls import path
from . import views

urlpatterns = [
    path('lista/', views.familiareslist, name = "familiares_list"),
    path('coder/', views.inicio, name = "inicio")
    
]
