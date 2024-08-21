from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

# Create your views here.
class HomeView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        template_name = 'main/home.html'
        context = {}
        return render(request, template_name, context)