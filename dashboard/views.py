from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .forms import UserRegistrationForm
from .models import Button, ButtonClick
from datetime import date
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import logout
from django.utils import timezone


def home(request):
    if request.user.is_authenticated:
        return redirect('buttons')
    return redirect('login')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('buttons')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('buttons')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def buttons(request):
    user = request.user
    buttons = Button.objects.all()

    for button in buttons:
        if ButtonClick.objects.filter(user=user, button=button, clicked_date=date.today()).exists():
            button.clicked = True
        else:
            button.clicked = False

    return render(request, 'buttons.html', {'buttons': buttons})



def button_click(request, button_id):
    button = Button.objects.get(id=button_id)
    user = request.user

    # Check if the user has already clicked the button today
    if not ButtonClick.objects.filter(user=user, button=button, clicked_date=date.today()).exists():
        ButtonClick.objects.create(user=user, button=button)
        return JsonResponse({'success': True, 'link': button.link})
    
    return JsonResponse({'success': False})


def user_logout(request):
    logout(request)
    return redirect('login')


@staff_member_required
def add_button(request):
    if request.method == 'POST':
        title = request.POST['title']
        link = request.POST['link']
        Button.objects.create(title=title, link=link, created_by=request.user)
        return redirect('buttons')
    return render(request, 'add_button.html')