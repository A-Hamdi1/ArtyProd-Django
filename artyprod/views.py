from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from artyweb.forms import UserRegistrationForm
from django.contrib import messages
from django.contrib.auth import login, authenticate

@login_required
def home(request):
    return render(request, 'home.html')

#--------------------------------------------REGISTER----------------------------------------------------------------------

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = user.username
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Bienvenue, {username} ! Votre compte a été créé avec succès.')
                return redirect('home')
            else:
                messages.error(request, 'Une erreur est survenue lors de la connexion.')
        else:
            messages.error(request, 'Une erreur est survenue lors de la validation du formulaire.')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})
