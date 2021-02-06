from django.urls import path
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView

import tracker_app.views as tracker_views


app_name = "tracker_app"
urlpatterns = [
  path("", tracker_views.HomeView.as_view(), name="home"),
  path("signup/", tracker_views.SignupView.as_view(), name="signup"),
  path("login/", LoginView.as_view(), name="login"),
  path("logout/", login_required(LogoutView.as_view()), name="logout"),
  path(
    "<int:pk>/", 
    tracker_views.ExerciseDetailView.as_view(), 
    name="exercise_detail")
]