""" ToDo views """
from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout


def home(request):
    """ Redner home page """
    return render(request, 'todo/home.html')


def signupuser(request):
    """ sign up user """
    if request.method == 'GET':
        return render(request, 'todo/signupuser.html', {'form': UserCreationForm()})

    form = UserCreationForm(request.POST)

    if form.is_valid():
        form.save()
        login(request, form.instance)
        return redirect('currenttodos')

    return render(request, 'todo/signupuser.html', {'form': form})


def loginuser(request):
    """ Login user """
    if request.method == 'GET':
        return render(request, 'todo/loginuser.html', {'form': AuthenticationForm()})

    form = AuthenticationForm(request, data=request.POST)

    if not form.is_valid():
        login(request, form.get_user())
        return redirect('currenttodos')

    return render(request, 'todo/loginuser.html', {'form': form})


def currenttodos(request):
    """ Render current ToDos page """
    return render(request, 'todo/currenttodos.html')


def logoutuser(request):
    """ Logout user """
    if request.method == 'POST':
        logout(request)
        return redirect('home')

    return redirect(request, 'todo/currenttodos.html')
