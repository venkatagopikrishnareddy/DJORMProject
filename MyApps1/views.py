from django.shortcuts import render
from django.db.models import Q
from django.db.models import Avg, Sum, Max, Min, Count
from MyApps1.models import Employee

# Create your views here.
def display_view(request):
    avg1=Employee.objects.all().aggregate(Avg('sal'))
    max=Employee.objects.all().aggregate(Max('sal'))
    min=Employee.objects.all().aggregate(Min('sal'))
    sum=Employee.objects.all().aggregate(Sum('sal'))
    count=Employee.objects.all().aggregate(Count('sal'))
    my_dict={'avg1':avg1,'max':max,'min':min,'sum':sum,'count':count}
    return render(request,'MyApps1/aggregate.html',my_dict)

def show_view(request):
    # ename = Employes.objects.get(ename='ram')
    # ename=Employee.objects.get(ename__iexact='Ram')
    #ename=Employee.objects.filter(ename__contains='R')
    #ename= Employee.objects.all()
    #ename=Employee.objects.filter(ename__regex='[A-Za-z]\w{2}')
    ename=Employee.objects.filter(ename__startswith='R')
    # ename=Employee.objects.filter(ename__startswith='R') | Employee.objects.filter(sal__lte=4500)
    # empno=Employee.objects.get(id__exact=6)
    # empno=Employee.objects.get(id=1)
    #empno = Employee.objects.all()
    empno=Employee.objects.filter(id__gt=4)
    #sal = Employee.objects.all()
    sal=Employee.objects.filter(sal__gt=50000)
    #address = Employee.objects.all()
    address=Employee.objects.filter(address__endswith='d')
    #job=Employee.objects.filter(ename__startswith='R') | Employee.objects.filter(sal__lte=4500)
    job=Employee.objects.all().values_list('ename','sal')
    my_dict={'ename':ename,'empno':empno,'sal':sal,'address':address,'job':job}
    return render(request, 'MyApps1/orm.html', my_dict)
