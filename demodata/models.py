from django.db import models

# Create your models here.
class Students(models.Model):
    stu_num=models.CharField(max_length=15,verbose_name="学号")
    name=models.CharField(max_length=20,verbose_name="姓名")
    out_data=models.DateTimeField(verbose_name="出生日期")
    age=models.IntegerField(verbose_name="年龄")
    sex=models.IntegerField(verbose_name="性别")  #1代表男,0代表女
    study_subject=models.CharField(max_length=32,verbose_name="学习科目")
    email=models.EmailField(null=True,verbose_name='邮箱')

    class Meta:
        db_table="students"

class Teachers(models.Model):
    t_name=models.CharField(max_length=20,verbose_name="老师姓名")
    t_subject=models.CharField(max_length=32,verbose_name="授课科目")

    class Meta:
        db_table="teachers"


