from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from tracker_app.models import Exercise


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

# TODO - update template with exercise stuff
class ExerciseDetailView(DetailView):
  model = Exercise
  context_object_name = "exercise"

# TODO - add create view, template, and url
class ExerciseCreateView(CreateView): pass


class ExerciseUpdateView(UpdateView): pass


class ExerciseDeleteView(DeleteView): pass


class ExerciseListView(ListView): pass