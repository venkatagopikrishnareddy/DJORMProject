from django.db import models

# Create your models here.
class Employee(models.Model):
    empno=models.IntegerField();
    ename=models.CharField(max_length=50);
    job=models.CharField(max_length=50);
    sal=models.FloatField();
    address=models.CharField(max_length=100);
    def __str__(self):
        return str(self.empno)+" "+self.ename+" "+str(self.sal)+" "+self.job+" "+self.address;
