from django.shortcuts import redirect, render
from vluchten import mixins
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login, logout

from api import forms

def Login(request):
    # cant see lander page if already logged in
    if request.user:
        if request.user.is_authenticated:
            return redirect("dashboard")

    form = forms.LoginForm(request.POST or None)

    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("dashboard")
        else:
            form.add_error(None, "Gebruikersnaam of wachtwoord is incorrect")

    return render(request, "main/login.html", {"form": form})


def LandingView(request):
    # cant see lander page if already logged in
    if request.user:
        if request.user.is_authenticated:
            return redirect("dashboard")

    # redirect to login otherwise
    return redirect("login")

class DashboardView(mixins.LogoutIfNotStaffMixin, TemplateView):
    template_name = "main/dashboard.html"
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, context=self.get_context_data(request))
    
    def get_context_data(self, request, **kwargs):
        context = super().get_context_data(**kwargs)
        
        if request.META.get('HTTP_HX_REQUEST'):
            context["HTMX"] = True

        return context
