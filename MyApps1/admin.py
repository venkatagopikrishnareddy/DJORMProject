from django.contrib import admin
from MyApps1.models import Employee

# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['empno','ename','job','sal','address'];

admin.site.register(Employee,EmployeeAdmin);
#admin.site.register(Employee);
