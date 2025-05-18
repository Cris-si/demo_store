from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.

@login_required
def profile(request):
    return render(request, 'accounts/profile.html')

@login_required
def edit_profile(request):
    return render(request, 'accounts/edit_profile.html')

@login_required
def order_history(request):
    return render(request, 'accounts/order_history.html')
