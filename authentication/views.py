# authentication/views.py
from django.contrib.auth import login, authenticate
from django.shortcuts import render

from . import forms


def login_page(request):
    # Gestion de la requete par défaut - GET
    form = forms.LoginForm()
    message = ""
    # Gestion de la requete POST
    if request.method == "POST":
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(  # Vérifie l'authenticité du couple nom/pwd
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password"],
            )
            if user is not None:
                login(request, user)  # Gère la connexion de l'utilisateur authentifié à la requête
                message = f"Bonjour, {user.username}! Vous êtes connecté."
            else:
                message = "Identifiants invalides."
    # Retour en cas de GET ou POST sans erreur
    return render(
        request, "authentication/login.html", context={"form": form, "message": message}
    )
