from django.urls import path
from . import views

app_name = 'adminapp'  # Define the namespace here

urlpatterns = [
    path('admin/', views.admin_home, name='admin'), 
    path('show_product/', views.show_prduct, name='show_prduct'), 
]