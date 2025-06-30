from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Emp, Project, Client, Deposit, Withdraw, Task
# website/views.py

def update_employee_profile(request):
    emp_id = request.session.get('emp_id')
    if not emp_id:
        return redirect('employee_login')

    try:
        emp = Emp.objects.get(employee_id=emp_id)
    except Emp.DoesNotExist:
        return redirect('employee_login')

    if request.method == 'POST':
        new_password = request.POST.get('password')
        new_image = request.FILES.get('img')

        if new_password:
            emp.employee_pass = new_password
        
        if new_image:
            emp.img = new_image

        emp.save()
        messages.success(request, 'Profile updated successfully.')
        return redirect('employee_dashboard')

    return render(request, 'website/employee_profile_update.html', {'emp': emp})

def employee_login(request):
    if request.method == 'POST':
        emp_id = request.POST.get('emp_id')
        emp_pass = request.POST.get('emp_pass')

        try:
            emp = Emp.objects.get(employee_id=emp_id, employee_pass=emp_pass)
            request.session['emp_id'] = emp.employee_id  # Store in session
            return redirect('employee_dashboard')
        except Emp.DoesNotExist:
            return render(request, 'website/employee_login.html', {'error': 'Invalid Employee ID or Password'})

    return render(request, 'website/employee_login.html')

def employee_dashboard(request):
    emp_id = request.session.get('emp_id')
    if not emp_id:
        return redirect('employee_login')

    try:
        emp = Emp.objects.get(employee_id=emp_id)
    except Emp.DoesNotExist:
        return redirect('employee_login')

    filter_status = request.GET.get('status')

    if filter_status == 'completed':
        tasks = Task.objects.filter(assigned_to=emp, is_completed=True).order_by('-created_on')
    elif filter_status == 'pending':
        tasks = Task.objects.filter(assigned_to=emp, is_completed=False).order_by('-created_on')
    else:
        tasks = Task.objects.filter(assigned_to=emp).order_by('-created_on')

    total_tasks = Task.objects.filter(assigned_to=emp).count()
    completed_tasks = Task.objects.filter(assigned_to=emp,  is_completed=True).count()
    running_tasks = total_tasks - completed_tasks

    context = {
        'emp': emp,
        'tasks': tasks,
        'filter_status': filter_status,
        'total_tasks': total_tasks,
        'completed_tasks': completed_tasks,
        'running_tasks':running_tasks,
    }
    return render(request, 'website/employee_dashboard.html', context)

def employee_logout(request):
    request.session.flush()
    return redirect('employee_login')

def admin_logout(request):
    request.session.flush()
    return redirect('index')

def login_view(request):
        if request.method == 'POST':
                username = request.POST.get('username')
                password = request.POST.get('password')

                user = authenticate(request, username=username, password=password)
                
                if user is not None:
                        login(request, user)
                        return redirect('index')  
                else:
                        messages.error(request, 'Invalid username or password.')
        return render(request, 'website/login.html')  
        
@login_required
def index(request):
        
       
        withdraw = Withdraw.objects.all().order_by('-created_on')[:5]
        dep = Deposit.objects.all().order_by('-created_on')[:5]
        pro = Project.objects.all().order_by('-created_on')
        total_withdraw = sum(w.amount for w in withdraw)
        total_deposit = sum(d.pay for d in dep)
        total_revenue = total_deposit-total_withdraw
        total_projects = Project.objects.count() 
        total_employee = Emp.objects.count() 
        total_client = Client.objects.count() 
        completed_projects = Project.objects.filter(status='completed').count()
        

        context = {
        'dep': dep,
        'withdraw': withdraw,
        'pro':pro,
        'total_deposit': total_deposit,
        'total_withdraw': total_withdraw,
        'total_revenue' : total_revenue,
        'total_projects': total_projects,
        'total_employee':total_employee,
        'total_client':total_client,
        'completed_projects':completed_projects,
        }
        return render(request, 'website/index.html', context)

@login_required
def project(request):
        pro = Project.objects.all().order_by('-created_on')
        return render(request, 'website/project.html',{'pro':pro})

@login_required
def deposit(request):
        dep = Deposit.objects.all().order_by('-created_on')
        return render(request, 'website/deposit.html',{'dep':dep})

@login_required
def revenue(request):
        withdraw = Withdraw.objects.all().order_by('-created_on')
        dep = Deposit.objects.all().order_by('-created_on')

        total_withdraw = sum(w.amount for w in withdraw)
        total_deposit = sum(d.pay for d in dep)
        total_revenue = total_deposit-total_withdraw

        context = {
        'dep': dep,
        'withdraw': withdraw,
        'total_deposit': total_deposit,
        'total_withdraw': total_withdraw,
        'total_revenue' : total_revenue,
        }
        return render(request, 'website/revenue.html', context)

@login_required
def client(request):
        client = Client.objects.all().order_by('-created_on')
        return render(request, 'website/client.html',{'client':client})

@login_required
def withdraw(request):
        withdraw = Withdraw.objects.all().order_by('-created_on')
        return render(request, 'website/withdraw.html',{'withdraw':withdraw})

@login_required
def forgot(request):
        return render(request, 'website/forgot.html')

@login_required
def employee(request):
        emp = Emp.objects.all().order_by('-created_on')
        return render(request, 'website/employee.html',{'emp':emp})

def search_results(request):
    query = request.GET.get('q', '')
    emp_results = client_results = project_results = []

    if query:
        emp_results = Emp.objects.filter(name__icontains=query)
        client_results = Client.objects.filter(name__icontains=query)  # 🔧 fixed here
        project_results = Project.objects.filter(project_name__icontains=query)

    return render(request, 'website/search_results.html', {
        'query': query,
        'emp_results': emp_results,
        'client_results': client_results,
        'project_results': project_results
    })

def adminEmployeeLogin(request):
        return render(request, 'website/adminEmployeeLogin.html')
