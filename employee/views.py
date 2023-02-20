from django.shortcuts import render, redirect
from django.contrib.auth import login
from .models import Employee
from .forms import EmployeeForm



def loginuser(request):
    if request.method == 'POST':
        try:
            print(request.POST.get('username'))
            print(request.POST.get('password'))
            # form = EmployeeForm 
            # print(form.username)
            # print(EmployeeForm(request.get['username']))
            user = Employee.objects.get(username=request.POST.get('username'), 
                                            # position=request.GET.get('position'), 
                                            password=request.POST.get('password') )
            login(request, user)
            return redirect('/addproduct')
        except Employee.DoesNotExist:
            return render(request, 'login.html', {'form':EmployeeForm(), "error": "User not found"})
    else:
        print('Please')
        return render(request, 'login.html', {'form': EmployeeForm()})

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
                
    
        


 