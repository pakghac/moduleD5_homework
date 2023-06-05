from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView
from .forms import BaseRegisterForm


# Create your views here.
class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'authorized_user_page.html'


class BaseRegisterView(CreateView):
    model = User
    form_class = BaseRegisterForm
    success_url = '/'



