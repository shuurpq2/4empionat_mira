from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError
from .validators import validate_image_size

class Course(models.Model):
  title = models.CharField("Название", max_length=30)
  description = models.CharField("Описание", max_length=100, blank=True, null=True)
  duration = models.PositiveIntegerField("Продолжительность (ч)", validators=[MaxValueValidator(10)])
  price = models.DecimalField("Цена", validators=[MinValueValidator(100)])
  start_date = models.DateTimeField("Дата начала")
  end_date = models.DateTimeField("Дата окончания")
  cover = models.ImageField("Обложка", upload_to="courses/covers/", validators=[validate_image_size])

  def clean(self):
    super().clean()

    if self.start_date and self.end_date:
      if self.start_date > self.end_date: raise ValidationError({"end_date": "Дата окончания должна быть позже даты начала"})

  def __str__(self):
    return f"{self.title}"