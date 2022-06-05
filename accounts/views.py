from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login
from .forms import SignUpForm
from django.contrib import messages


# Create your views here.
def signup(request):
  if request.method == 'POST':
    form = SignUpForm(request.POST)
    if form.is_valid():
      user = form.save()
      messages.success(request, 'Account was created for ' + str(user))
      auth_login(request, user)
      return redirect('/')
    else:
      return render(request, 'signup.html', {'form': form})
  else:
    form = SignUpForm()
    return render(request, 'signup.html', {'form': form})