from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
# login函数重命名为auth_login以避免与内置login视图冲突
from django.contrib.auth import login as auth_login


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

