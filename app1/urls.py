from django.urls import path
from . import views

urlpatterns = [
    path('',views.ram,name='ram'),
    
]
