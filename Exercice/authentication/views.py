from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import EmailMessage, send_mail
from website import settings
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_text
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def home(request):
    return render(request, "authentication/signin.html")

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        pass1 = request.POST['pass1']
        
        if User.objects.filter(username=username):
            messages.error(request, "Utilisateur existe déjà")
           # return redirect('home')
        
        if len(pass1) < 8:
            messages.error(request, "Votre mot de passe doit être supérieur à 8 caractères")
           # return redirect('home')
        
        myuser = User.objects.create_user(username, email, pass1)
        myuser.is_active = False
        myuser.save()
        messages.success(request, "Ajout de compte")
        #return redirect('login')
        
        
    return render(request, "authentication/signin.html")

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']
        user = authenticate(username=username, password=pass1)
        
        if user is not None:
            login(request, user)
            messages.success(request, "OK")
            return redirect("home")
        else:
            messages.error(request, "Erreur.Recommencer!!")
            return redirect('home')
    
    return render(request, "authentication/signin.html")