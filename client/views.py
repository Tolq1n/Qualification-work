from django.shortcuts import render, redirect
from .models import Client
from .forms import ClientForm


def create_client(request):
    
    if request.method == "GET":
        form = ClientForm
        return render(request, 'clients/client.html', {'form':form})
    else:
        print("hi")
        try:
            form = ClientForm(request.POST)
            form.save()
            return redirect('show_clients')
        except ValueError:
            return render(request, 'clients/client.html', {'form': form, 'error':'Bad request passed in.Try again'})
        
def add_client(request):
    if request.method == "POST":
        try:
            form = ClientForm(request.POST)
            form.save()
            return redirect('show_clients')
        except ValueError:
            return render(request, 'clients/client.html', {'form': form, 'error':'Bad request passed in.Try again'})        

def show_clients(request):
    clients = Client.objects.all()
    return render(request, 'clients/clients.html', {'clients':clients})


