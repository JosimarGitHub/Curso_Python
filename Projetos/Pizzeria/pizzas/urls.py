"""Defines URLs patterns for pizzas"""


from django.urls import path
from . import views

app_name = 'pizzas' 

urlpatterns = [ 
    # Home page 
    path('', views.index, name='index'),
    # Detail page for a pizza topping.
    path('index/<int:pizza_id>/', views.pizza_top, name='pizza_top'), 
]
