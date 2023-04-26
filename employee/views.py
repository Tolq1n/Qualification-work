from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .models import Employee
from .forms import EmployeeForm
from order.forms import OrderForm
from manifactured_product.forms import ManufacturedProductForm



def loginpage(request):
    if request.method == 'POST':
        try:
            print(request.POST.get('username'))
            print(request.POST.get('password'))
            print(request.POST.get('position'))
            # form = EmployeeForm 
            # print(form.username)
            # print(EmployeeForm(request.get['username']))
            user = Employee.objects.get(username=request.POST.get('username'), 
                                            position=request.POST.get('position'), 
                                            password=request.POST.get('password') )
            print(user.username, 'login successful')
            login(request, user)
            position = request.POST.get('position')
            if position == '1':
                return render(request, 'order/order.html', {'form':OrderForm()})
            else:
                return render(request, 'manifactured_product/manufactured_product.html', {'form':ManufacturedProductForm()})
            
        except Employee.DoesNotExist:
            return render(request, 'login.html', {'form':EmployeeForm(), "error": "User not found"})
    else:
        print('Please')
        return render(request, 'login.html', {'form': EmployeeForm()})
    
def logoutuser(request):
    if request.method == 'GET':
        logout(request)
        return redirect('/')

                
    
        


 