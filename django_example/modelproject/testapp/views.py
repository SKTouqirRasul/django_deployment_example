from django.shortcuts import render
from testapp import models
# Create your views here.
def employee_View(request):

    emp_info = models.Employee.objects.all()

    return render(request, 'testapp/result.html',{'emp':emp_info})
