from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError
from apps.students.models import Student
from .validators import validate_image_size, validate_supertube_link
from PIL import Image
import os

class Course(models.Model):
  title = models.CharField("Название", max_length=30)
  description = models.CharField("Описание", max_length=100, blank=True, null=True)
  duration = models.PositiveIntegerField("Продолжительность (ч)", validators=[MaxValueValidator(10, "Максимальная продолжительность курса 10 часов")])
  price = models.DecimalField("Цена", validators=[MinValueValidator(100, "Минимальная стоимость курса 100 рублей")])
  start_date = models.DateTimeField("Дата начала")
  end_date = models.DateTimeField("Дата окончания")
  cover = models.ImageField("Обложка", upload_to="courses/covers/", validators=[validate_image_size])
  students = models.ManyToManyField(Student, through="Enrollment")

  def clean(self):
    super().clean()

    if self.start_date and self.end_date:
      if self.start_date > self.end_date:
        raise ValidationError({"end_date": "Дата окончания должна быть позже даты начала"})

  def save(self, *args, **kwargs):
    super().save(*args, **kwargs)

    if self.cover:
      img_path = self.cover.path
      output_size = (300, 300)

      with Image.open(img_path) as img:
        folder, filename = os.path.split(img_path)
        thumb_path = os.path.join(folder, f"mpic{filename}")
        
        img.thumbnail(output_size)
        img.save(thumb_path)

  def __str__(self):
    return f"{self.title}"

class Lesson(models.Model):
  title = models.CharField("Название", max_length=50)
  text_content = models.CharField("Содержание")
  video_link = models.CharField("Видеоссылка SuperTube", validators=[validate_supertube_link], blank=True, null=True)
  duration = models.PositiveIntegerField("Длительность (ч)", validators=[MaxValueValidator(4, "Максимальная длительность урока 4 часа")])
  course = models.ForeignKey(Course, verbose_name="Курс", on_delete=models.CASCADE, related_name="lessons")

  def clean(self):
    super().clean()

    if self.course:
      course_lessons = self.course.lessons.all()

      if self not in course_lessons and len(course_lessons) >= 5:
        raise ValidationError({"course": "Превышено максимальное количество уроков в одном курсе (5)"})

  def __str__(self):
    return f"{self.title}"

class Enrollment(models.Model):
  student = models.ForeignKey(Student, verbose_name="Студент", on_delete=models.CASCADE, related_name="enrollments")
  course = models.ForeignKey(Course, verbose_name="Курс", on_delete=models.CASCADE, related_name="enrollments")