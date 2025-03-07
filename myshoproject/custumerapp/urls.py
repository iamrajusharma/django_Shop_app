from django.urls import path
from . import views

app_name = 'custumerapp'  # Define the namespace here

urlpatterns = [
    path('custumer/', views.customer_home, name='custumer'),  # Example route
]