from django.shortcuts import render, redirect
from .models import ManufacturedProduct
from .forms import ManufacturedProductForm

def manufacturedmroduct(request):
    form = ManufacturedProductForm
    return render(request, 'manifactured_product/manufactured_product.html', {'form': form})

def add_mproduct(request):
    if request.method == 'POST':
        try:
            form = ManufacturedProductForm(request.POST)
            form.save()
            return redirect('show_mproduct')
        except ValueError:
            return render(request, 'manifactured_product/manufactured_product.html', {'form': form, 'error':'Bad request passed in.Try again'})

def show_mproduct(request):
    products = ManufacturedProduct.objects.all()
    return render(request, 'manifactured_product/show_mproduct.html', {'products': products})
        
