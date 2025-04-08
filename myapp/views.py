from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import empdata
from django.http import HttpResponseNotFound

@login_required(login_url='login')
def HomePage(request):
    return render(request, 'home.html')

def custom_404_view(request, exception):
    return render(request, 'errors/404.html', status=404)

def block_view(request):
    return HttpResponseNotFound("This page is blocked.")

def signup(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        address = request.POST['address']
        contactno = request.POST['contactno']
        location = request.POST['location']

        if not all([name, email, password, address, contactno, location]):
            messages.error(request, "All fields are required!")
            return redirect('signup')

        # Check if user with the same name or email already exists
        if User.objects.filter(username=name).exists() or User.objects.filter(email=email).exists():
            messages.error(request, "Username or Email already exists!")
            return redirect('signup')
    
        user = User.objects.create_user(username=name, email=email, password=password)
        user.save()
        empdata.objects.create(
            name=name,
            email=email,
            password=password,
            address=address,
            contact_no=contactno,
            location=location
        )
        messages.success(request, "Account created successfully! You can now log in.")
        return redirect('login')
    return render(request, 'signup.html')

def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('name')
        password = request.POST.get('password')

        if not username or not password:
            messages.error(request, "Both fields are required!")
            return redirect('signup')

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password!")
    return render(request, 'signup.html')
        
def logoutpage(request):
    logout(request)
    return redirect('login')

def frontpage(request):
    return render(request,'frontpage.html')