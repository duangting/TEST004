from django.db import models

# Create your models here.
#设计model

class Employee(models.Model):

    id=models.IntegerField(primary_key=True,verbose_name='id')
    name=models.CharField(max_length=10,verbose_name='姓名')
    sex=models.CharField(max_length=10,verbose_name='性别')
    email=models.EmailField(max_length=30,verbose_name='邮箱')
    create_date=models.DateField(auto_now_add=True,verbose_name='入职日期')
    update_date=models.DateTimeField(auto_now=True,verbose_name='更新时间')

    class Meta:
        verbose_name='姓名'
        verbose_name_plural=verbose_name

