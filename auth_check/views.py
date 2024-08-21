from django.conf import settings
from django.contrib.auth import get_user_model, views, authenticate, login
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import View

from . import forms

User = get_user_model()

class LoginView(View):
    def get(self, request):
        form = forms.LoginForm()
        return render(request, 'registration/login.html', {'form': form})
    def post(self, request):
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            username_or_email = form.cleaned_data['username_or_email']
            password = form.cleaned_data['password']
            
            # Try to authenticate with username
            user = authenticate(request, username=username_or_email, password=password)
            
            if user is None:
                # If no user found, try to authenticate with email
                try:
                    user_obj = get_user_model().objects.get(email=username_or_email)
                    user = authenticate(request, username=user_obj.username, password=password)
                except get_user_model().DoesNotExist:
                    user = None
            
            if user is not None:
                login(request, user)
                return redirect('/')  # Redirect to a success page.
            else:
                form.add_error(None, "Invalid username/email or password")
                
        return render(request, 'registration/login.html', {'form': form})

class LogoutView(views.LogoutView):
    pass

class PasswordResetView(views.PasswordResetView):
    success_url = reverse_lazy("accounts:password_reset_done")
    html_email_template_name = 'registration/password_reset_email.html'

class PasswordResetDoneView(views.PasswordResetDoneView):
    pass

class PasswordResetConfirmView(views.PasswordResetConfirmView):
    success_url = reverse_lazy("accounts:password_reset_complete")

class PasswordResetCompleteView(views.PasswordResetCompleteView):
    pass

class PasswordChangeView(views.PasswordChangeView):
    success_url = reverse_lazy("accounts:password_change_done")

class PasswordChangeDoneView(views.PasswordChangeDoneView):
    pass
