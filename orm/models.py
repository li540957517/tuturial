from django.db import models


# Create your models here.

class Employee(models.Model):
    DEPARTMENTS = (
        ('管理部', '管理部'),
        ('营销部', '营销部'),
        ('业务部', '业务部'),
        ('生产制造部', '生产制造部'),
    )
    name = models.CharField('姓名', max_length=20)
    idcard = models.CharField('身份证号', max_length=20)
    department = models.CharField('部门', choices=DEPARTMENTS,max_length=50)
    salary = models.DecimalField('薪资', max_digits=9, decimal_places=2)
    address = models.CharField('地址', max_length=100, null=True)
    tel = models.CharField('电话', max_length=20)
    post_code = models.CharField('邮编', max_length=6)
    birthdate = models.DateTimeField('生日')

    class Meta:
        ordering = ['department', '-salary']

    def do_something(self):
        pass

    def __str__(self):
        return f'{self.id} {self.name} {self.department} {self.salary}'

    """"9.1-9.6   45:38"""
