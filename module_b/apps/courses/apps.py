from django.apps import AppConfig


class CoursesConfig(AppConfig):
    name = 'apps.courses'
    verbose_name = "Курсы и уроки"

    def ready(self):
        import apps.courses.signals
