import os

from django.contrib import messages
from django.contrib.auth import login, authenticate, update_session_auth_hash
from django.views.generic import ListView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.views.generic.edit import UpdateView
from django.shortcuts import render, get_object_or_404
from .models import *
from .forms import *
from django.conf import settings
from django.contrib.auth.forms import PasswordChangeForm



class MainView(ListView):
    model = Cat
    template_name = 'index.html'

    def get_context_data(self, *args, **kwargs):
        context = {'Catlist': Cat.objects.all()}
        return context


class ProfileView(ListView):
    model = Cat
    template_name = 'profileview.html'

class UserRegView(CreateView):
    form_class = SignUpForm
    template_name = 'registration/registration.html'
    success_url = '../../account/login/'

class ProfileCatsView(ListView):
    model = Cat
    template_name = 'person_Cat.html'
    def get_context_data(self, *args, **kwargs):
        context = {'Catlist': Cat.objects.all().filter()}
        return context

def Cat_detail(request, pk):
    cat_instance = get_object_or_404(Cat, pk=pk)
    hostnameclean = ' '.join(str(cat_instance.hostname).replace('_', '-').split('-'))
    return render(request, 'Cat_detail.html', {'Cat': cat_instance, 'hostname': hostnameclean})

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Пароль изменен успешно!')
            return redirect('change_password')
        else:
            messages.error(request, 'Неверный ввод.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change_password.html', {
        'form': form
    })






