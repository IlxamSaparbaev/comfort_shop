from django.shortcuts import render
from django.contrib.auth import login, authenticate
from .forms import LoginForm
from django.http import HttpResponse

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Аутентификация прошла успешно.')
                else:
                    return HttpResponse('Несуществущий аккаунт.')
            else:
                HttpResponse('Неверный логин.')
    else:
        form = LoginForm()
    context = {
        'form': form
    }
    return render(request, 'account/login.html', context)