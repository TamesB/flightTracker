from django.shortcuts import redirect, render
from . import mixins
from django.views.generic import TemplateView


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
