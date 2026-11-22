from django.test import TestCase
from .models import Student

class StudentModelTest(TestCase):
  def setUp(self):
    self.student_first_name = "ab"
    self.student_last_name = "fds"
    self.student_mid_name = "gfds"

    self.student = Student.objects.create(
      first_name=self.student_first_name,
      last_name=self.student_last_name,
      mid_name=self.student_mid_name,
    )

  def test_student_creation(self):
    self.assertEqual(self.student.first_name, self.student_first_name)
    self.assertEqual(self.student.last_name, self.student_last_name)
    self.assertEqual(self.student.mid_name, self.student_mid_name)