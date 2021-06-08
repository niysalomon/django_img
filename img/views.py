from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages


# Create your views here.
def index(request):
    pass

    return render(request,'index.html')
def register(request):
    if request.method == 'POST': 
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        retype_password = request.POST['retype_password']

        if password == retype_password:
            if User.objects.filter(email=email).exists():
                messages.info(request,'Email taken')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request,'Username is taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                return redirect('login')
        else:
            messages.info(request,'Check your username or email!')
            return redirect('register')
    else:
        return render(request,'form.html')
def login(request):
    if request.method =="POST":
        username =request.POST['username']
        password =request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Wrong credentials!!')
            return redirect('login')

    return render(request,'login.html')
def logout(request):
    auth.logout()
    redirect('login')
