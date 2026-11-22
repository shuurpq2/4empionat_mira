from django.db import models
from django.conf import settings

class Student(models.Model):
  first_name = models.CharField("Имя", max_length=32)
  last_name = models.CharField("Фамилия", max_length=32)
  mid_name = models.CharField("Отчество", max_length=32)
  user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="student")

  def __str__(self):
    return f"{self.last_name} {self.first_name} {self.mid_name}"