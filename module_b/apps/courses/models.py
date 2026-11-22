from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Course(models.Model):
  title = models.CharField("Название", max_length=30)
  description = models.CharField("Описание", max_length=100, blank=True, null=True)
  duration = models.PositiveIntegerField("Продолжительность (ч)", validators=[MaxValueValidator(10)])
  price = models.DecimalField("Цена", validators=[MinValueValidator(100)])
  start_date = models.DateTimeField("Дата начала")
  end_date = models.DateTimeField("Дата окончания")
  img = models.ImageField("Обложка", upload_to="courses/covers/")

  def __str__(self):
    return f"{self.title}"