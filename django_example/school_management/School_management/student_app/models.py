from django.db import models

# Create your models here.
class School(models.Model):
    school_name = models.CharField(max_length=256)

    def __str__(self):
        return self.school_name


class Student_details(models.Model):
    student_name = models.CharField(max_length= 50)
    student_age = models.IntegerField()
    student_rollNo = models.IntegerField(primary_key=True)
    school_name = models.ForeignKey(School,on_delete=models.CASCADE,related_name='student')

    def __str__(self):
        return self.student_name
