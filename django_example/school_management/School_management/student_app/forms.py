from django import forms
from student_app.models import School
from django.contrib.auth.models import User

class School_Form(forms.ModelForm):

    class Meta():
        model = School
        fields = (school_name)

class Student_details_Form(forms.ModelForm):

    class Meta():
        model = Student_details
        fields = (student_name,student_age,student_rollNo,school_name)

class User_Form(forms.ModelForm):
    class Meta():
        model = User
        fields = (username,first_name,last_name,email,password)
