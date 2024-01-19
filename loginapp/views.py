from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth import get_user_model

User = get_user_model()

def signup(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        full_name = request.POST.get('full_name')
        phone_number = request.POST.get('phone_number')
        password = request.POST.get('password')

        user = User.objects.create_user(username = username, full_name = full_name, phone_number=phone_number, password = password)
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