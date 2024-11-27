from django.db import models

# Create your models here.
class UserInfo(models.Model):
    # 定义名字
    name = models.CharField(max_length=15)
    # 年龄
    ogz = models.CharField(max_length=20)
    #  性别
    gender = models.DateField(max_length=2)
    #  爱好
    love = models.CharField(max_length=50)
    # adress = models.CharField(max_length=20)
    # 手机号码
    tel = models.IntegerField(default=0)
    # 服务时间
    s_time = models.IntegerField(default=0)
    # 3
    is_delete = models.BooleanField(default=False)


    # def __str__(self):
    #     return self.name