from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View

# Create your views here.
class LoginViewCustom(LoginView):
    template_name = 'account/login.html'

class LogoutViewCustom(LogoutView):
    template_name = 'account/logout.html'

class AccountView(LoginRequiredMixin, View):
    model = User
    template_name = 'account/account.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'user': request.user})