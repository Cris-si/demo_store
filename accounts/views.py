from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

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

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'账号 {username} 创建成功！请登录。')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})
