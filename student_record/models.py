from django.db import models

# Create your models here.
class Faculty(models.Model):
    faculty_name = models.CharField(max_length=200)
    building = models.CharField(max_length=3)

class Course(models.Model):
    course_name = models.CharField(max_length=200)
    course_code = models.CharField(max_length=6)

class Student(models.Model):
    # Many to Many
    course = models.ManyToManyField(Course)
    # One to many
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    student_name = models.CharField(max_length=200)
    student_lastname = models.CharField(max_length=200)
    student_code = models.CharField(max_length=8)
    telephone_number = models.CharField(max_length=10)
