from django.shortcuts import render
from . models import Pizza

# Create your views here.
def index(request): 
    """The home page for Pizzas.""" 
    pizzas = Pizza.objects.all()
    context = {'pizzas': pizzas}
    return render(request, 'pizzas/index.xhtml',context)

def pizza_top(request, pizza_id):
    pizza = Pizza.objects.get(id=pizza_id)
    toppings = pizza.topping_set.all()
    context = {'pizza': pizza, 'toppings': toppings }
    return render(request, 'pizzas/pizza_top.xhtml', context)