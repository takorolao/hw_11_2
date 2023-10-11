from django.urls import path
from .views import generate_data

urlpatterns = [
    path('generate-data/', generate_data, name='generate-data'),
]
