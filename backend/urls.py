
from django.urls import path
from backend.views import show_index

urlpatterns = [
    path('show',show_index,name='show')
   
]