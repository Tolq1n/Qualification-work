from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .models import Employee
from .forms import EmployeeForm



def loginuser(request):
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
            login(request, user)
            position = request.POST.get('position')
            if position == '1':
                return redirect('/order')
            else:
                return redirect('addproduct')
            
        except Employee.DoesNotExist:
            return render(request, 'login.html', {'form':EmployeeForm(), "error": "User not found"})
    else:
        print('Please')
        return render(request, 'login.html', {'form': EmployeeForm()})
    
def logoutuser(request):
    if request.method == 'GET':
        logout(request)
        return redirect('loginuser')
# def login(request):
#      if request.method == 'POST':
#             try:
#                 print(request.GET.get('username'))
#                 print(request.GET.get('password'))
#                 user = Employee.objects.get(username=request.GET.get('username'), 
#                                             # position=request.GET.get('position'), 
#                                             password=request.GET.get('password') )
#                 print(user.username)
#                 return redirect('/addproduct')
#             except Employee.DoesNotExist:
#                   return render(request, 'login.html', {'form':EmployeeForm(), "error": "User not found"})
                
    
        


 