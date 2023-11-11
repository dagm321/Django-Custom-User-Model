from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate

def signup(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = User.objects.create_user(username = username, email = email, password = password)
        user.save()
        return redirect('loginpage')



    return render(request, 'signup.html')


def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse("wrong passoword or username")


    return render(request, 'login.html')

def home(request):
    return render(request, 'home.html')