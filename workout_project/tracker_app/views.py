from django.shortcuts import render
from django.views.generic.base import TemplateView

from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic.edit import FormView


class HomeView(TemplateView):
  template_name = "tracker_app/home.html"


class SignupView(FormView):
  form_class = UserCreationForm
  model = User
  template_name = "registration/signup.html"
  success_url = reverse_lazy("tracker_app:home")

  def form_valid(self, form):
    user = form.save()
    login(self.request, user)
    return super().form_valid(form)

