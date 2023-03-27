from django.shortcuts import render, redirect
from .models import Order
from .forms import OrderForm
# Create your views here.

def add_order(request):
    if request.method == 'POST':
        try:
            form = OrderForm(request.POST)
            form.save()
            return redirect('orders')
        except ValueError:
            return render(request, 'order/order.html', {'form': form})
    else:
        form = OrderForm
        return render(request, 'order/order.html', {'form': form})
    
def orders(request):
    orders = Order.objects.all()
    return render(request, 'order/orders.html', {'orders': orders})
