from django.shortcuts import render, redirect
from django.contrib import messages, auth
from contacts.models import Contact
from django.contrib.auth.models import User

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username = username, password = password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, "You are logged in.")
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid credentials.")
            return redirect('login')

    else:
        return render(request, 'accounts/login.html')

def register(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(username = username).exists():
                messages.error(request, "Username already taken.")
                return redirect('register')
            else:
                if User.objects.filter(username = username).exists():
                    messages.error(request, "Email already exists.")
                    return redirect('register')
                else:
                    user = User.objects.create_user(first_name = first_name, last_name = last_name, username = username, password=password, email=email)
                    user.save()
                    messages.success(request, "Successfully registered.")
                    return redirect('login')            

        else:
            messages.error(request, "Passwords do not match.")
            return redirect('register')
         
    else:
        return render(request, 'accounts/register.html')

def logout(request):
    if request.method == "POST":
        auth.logout(request)
        messages.success(request, "You are logged out.")
        return redirect('index')
    return redirect('index')

def dashboard(request):
    contacts = Contact.objects.order_by('-contact_date').filter(user_id = request.user.id)
    for i in contacts:
        print(i.listing)
    context = {
        'contacts':contacts
    }
    return render(request, 'accounts/dashboard.html',context)
