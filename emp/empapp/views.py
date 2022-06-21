from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.forms import UserCreationForm
from . import models

def index(request):
    events=models.Event.objects.all()
    return render(request, 'home.html',{'events':events})

def loginUser(request):
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')

        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Username OR password does not exit')

    return render(request, 'registration/login.html')


def logoutUser(request):
    logout(request)
    return redirect('/')

def sign_up(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'An error occurred during registration')

    return render(request, 'registration/sign-up.html',{'form': form})

def event_detail(request):
    ev_name=request.GET.get('ev_name')
    event=models.Event.objects.get(ev_name=ev_name)
    if request.method == 'POST':
        if request.user.is_authenticated:
            date=request.POST.get('date')
            location=request.POST.get('location')
            user=request.user
            booking=models.Booking(event=event,user=user,ev_date=date,ev_location=location)
            booking.save()
            messages.success(request, 'Booking successful')
            return redirect('/')
        else:
            messages.error(request, 'Please login to book')
            
    return render(request, 'event.html',{'event':event})

