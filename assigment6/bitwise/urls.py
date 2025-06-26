from django.urls import path
from .views import process_number

urlpatterns = [
    path('', process_number, name='process_number'),
]