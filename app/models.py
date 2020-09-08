from django.db import models

# Create your models here
class CourseModel(models.Model):
    course_no = models.IntegerField(primary_key=True)
    course_name = models.CharField(max_length=30)
    def __str__(self):
        return self.course_name

class StudentModel(models.Model):
 student_no = models.IntegerField(primary_key=True)
 name = models.CharField(max_length=30)
 contact = models.IntegerField()
 course = models.ManyToManyField(CourseModel)
 def __int__(self):
        return self.student_no
