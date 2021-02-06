from django.db import models
from django.contrib.auth.models import User


class Exercise(models.Model):
  name = models.CharField(max_length=100)
  sets = models.PositiveIntegerField()
  reps = models.PositiveIntegerField()
  weight = models.PositiveIntegerField()
  performed = models.DateTimeField(auto_now_add=True)
  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now_add=True)
  created_by = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
        return self.name