from email.headerregistry import Group
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

def loginPage(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = username, password= password)
        if user is not None:
            login(request, user)

            group = None
           
            group = user.groups.all()[0].name
            if group == 'admin':
                return redirect('dashboard')
            else:
                return redirect('index')
        else:
            messages.info(request, 'wrong username or password')
            return redirect('login')


    return render(request, 'app/login.html')



def registerPage(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.create(username = username, email = email, password = password)
        
        user.save()
        group = Group.object.get(name = 'user')
        user.groups.add(group)
        return redirect('login')
    return render(request, 'app/register.html')



@login_required(login_url='login')
def dashboard(request):
    return render(request, 'app/dashboard.html')


@login_required(login_url='login')
def index(request):
    return render(request, 'app/index.html')
