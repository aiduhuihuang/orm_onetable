from django.shortcuts import render
from django.http import  HttpResponse
from .models import *

# Create your views here.
#单表对学生的操作
#增加
def addstudents(request):
    #sava()
    stu=Students()
    stu.stu_num="stu1007"
    stu.name="王菲"
    stu.out_data="1991-2-3"
    stu.age=28
    stu.sex=1
    stu.study_subject="C#"
    stu.email=None
    stu.save()

    return HttpResponse("add对学生数据增加")

#查询
def getstudents(request):
    #all方法,返回queryset结果集
    # stu=Students.objects.all().first()
    # print(stu)

    # stus=Students.objects.get(age=22)
    # print(stus)

    #values
    stu=Students.objects.all().values()
    # print(stu.count())
    return render(request,"selecdata.html",{"stu":stu})
    # return HttpResponse("查询学生数据")


#修改
def updates(request):
    # stu=Students.objects.get(id=1)
    # stu.study_subject="C++"
    # stu.save()

    # stu=Students.objects.filter(age=22)
    # for one in stu:
    #     one.age=25
    #     one.save()

    # Students.objects.filter(age=25).update(age=21,study_subject="Go")
    stu=Students.objects.filter(age__gt=25)
    print(stu)



    return HttpResponse("修改学生数据")