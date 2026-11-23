from django.db.models.signals import pre_delete
from django.dispatch import receiver
from django.core.exceptions import ValidationError
from .models import Lesson

@receiver(pre_delete, sender=Lesson)
def handle_lesson_delete(sender, instance: Lesson, **kwargs):
    enrollments_count = len(instance.course.enrollments.all())
    if enrollments_count > 0:
        raise Exception(f"Невозможно удалить урок \"{instance}\" курса \"{instance.course}\", на который записаны студенты ({enrollments_count})")