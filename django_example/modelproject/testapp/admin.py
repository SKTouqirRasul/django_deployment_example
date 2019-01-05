from django.contrib import admin
from testapp import models
# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display=['eno','ename','esal','eaddr']


admin.site.register(models.Employee,EmployeeAdmin)
