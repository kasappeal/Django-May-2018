from django.contrib import messages
from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from django.contrib.auth import login as django_login, logout as django_logout

from users.forms import LoginForm


def login(request):
    """
    Muestra el formulario de login y procesa el login de un usuario
    :param request: objeto HttpRequest
    :return: objeto HttpResponse con el formulario renderizado
    """
    # si la petición es POST, entonces tenemos que hacer el login
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            # comprobamos si las credenciales son correctas
            user = authenticate(username=username, password=password)
            if user is None:
                messages.error(request, 'Usuario o contraseña incorrecto')
            else:
                # iniciamos la sesión del usuario (hacemos login del usuario)
                django_login(request, user)
                url = request.GET.get('next', 'home')
                return redirect(url)
    else:
        form = LoginForm()

    context = {'form': form}
    return render(request, 'users/login.html', context)


def logout(request):
    """
    Hace logout de un usuario y le redirige al login
    :param request: objeto HttpRequest
    :return: objeto HttpResponse de redirección al login
    """
    django_logout(request)
    return redirect('login')
