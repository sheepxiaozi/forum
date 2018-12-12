from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
# login函数重命名为auth_login以避免与内置login视图冲突
from django.contrib.auth import login as auth_login
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import UpdateView
from accounts.forms import UserInformationUpdateForm
from forms import SignUpForm


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


@method_decorator(login_required, name='dispatch')
class UserUpdateView(UpdateView):
    form_class = UserInformationUpdateForm
    template_name = 'my_account.html'
    success_url = reverse_lazy('my_account')

    def get_object(self):
        return self.request.user

