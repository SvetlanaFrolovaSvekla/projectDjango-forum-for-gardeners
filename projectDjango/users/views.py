from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .forms import LoginUserForm, RegisterUserForm

from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView

from django.contrib.auth.forms import AuthenticationForm

class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'users/login.html'
    extra_context = {'title': 'Авторизация'}
    success_url = reverse_lazy('home')


    # def get_success_url(self):
    #     return reverse_lazy('home')



def register(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return render(request, 'users/register_done.html')
    else:
        form = RegisterUserForm()
    return render(request, 'users/register.html', {'form': form})
