from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .models import Note


# ---------- INDEX ----------
def index(request):
    return render(request, 'index.html')


# ---------- ABOUT ----------
def about(request):
    return render(request, 'about.html')


# ---------- CONTACT ----------
def contact(request):
    return render(request, 'contact.html')


# ---------- SIGNUP ----------
def signup_view(request):
    if request.user.is_authenticated:
        messages.info(request, "You're already logged in.")
        return redirect('notes')  # redirect logged-in users to notes page

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # log in user immediately after signup
            messages.success(request, f"Welcome {user.username}! Your account has been created.")
            return redirect('notes')  # redirect to notes after signup
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = UserCreationForm()

    return render(request, 'signup.html', {'form': form})


# ---------- LOGIN ----------
def login_view(request):
    if request.user.is_authenticated:
        messages.info(request, "You're already logged in.")
        return redirect('notes')

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, f"Welcome back, {username}!")

                # Redirect to 'next' if available (Django automatically provides ?next=)
                next_url = request.GET.get('next') or reverse('notes')
                return redirect(next_url)
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})


# ---------- LOGOUT ----------
def logout_view(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect('login')


# ---------- NOTES ----------
@login_required(login_url='login')
def notes_view(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')

        if title and content:
            Note.objects.create(user=request.user, title=title, content=content)
            messages.success(request, "Note added successfully!")
            return redirect('notes')
        else:
            messages.error(request, "Both title and content are required.")

    notes = Note.objects.filter(user=request.user)
    return render(request, 'notes.html', {'notes': notes})
