# coding=utf-8

from django.db import models
from django.db import connection


# Create your models here.


# sql学校表操作类
class SckoolManageSql(models.Model):
    parent_id = models.PositiveSmallIntegerField(unique=True)
    name = models.CharField(max_length=50, unique=True)
    area = models.CharField(max_length=50, unique=True)
    edu_group = models.CharField(max_length=50, unique=True)
    period = models.CharField(max_length=50, unique=True)
    tel = models.CharField(max_length=50, unique=True)
    email = models.CharField(max_length=50, unique=True)
    cover = models.CharField(max_length=50, unique=True)
    remark = models.CharField(max_length=50, unique=True)
    status = models.PositiveSmallIntegerField(unique=True)
    deleted = models.PositiveSmallIntegerField(unique=True)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{'parent_id:%s,name:%s,area:%s,edu_group:%s,period:%s,tel:%s,mail:%s,cover:%s,remark:%s,status:%s,deleted:%s',create_at:%s>}" % (
            self.parent_id, self.name, self.area, self.edu_group, self.period, self.tel, self.email, self.cover,
            self.remark, self.status, self.deleted, self.create_at)

    class Meta:
        db_table = 'data_school'

    # 上传学校信息Excel文件插入数据库
    def SaveDataBase(ShoolData, ID_number):
        try:
            for data in ShoolData:
                list_ID_number = str(ID_number)
                list_name = data[0]
                list_area = data[1]
                list_edu_group = data[2]
                list_period = data[3]
                tel = data[4]
                list_tel = str(tel)
                email = data[5]
                list_email = str(email)
                print('开始导入')
                with connection.cursor() as sqls:
                    sqls.execute(
                        "insert into data_school(parent_id,name,area,edu_group,period,tel,email)" + " values('" + list_ID_number + "','" + list_name + "','" + list_area + "','" + list_edu_group + "','" + list_period + "','" + list_tel + "','" + list_email + "');");
                print('导入成功')
        except Exception as ErrorResult:
            print(ErrorResult)
            return '导入数据库异常'

    # 新增学校
    def SaveSchoolData(ShoolDatas, ID_number):
        try:
            list_ID_number = str(ID_number)
            list_name = ShoolDatas[0]
            list_area = ShoolDatas[1]
            list_edu_group = ShoolDatas[2]
            list_period = ShoolDatas[3]
            tel = ShoolDatas[4]
            list_tel = str(tel)
            email = ShoolDatas[5]
            list_email = str(email)
            with connection.cursor() as sqls:
                sqls.execute(
                    "insert into data_school(parent_id,name,area,edu_group,period,tel,email)" + " values('" + list_ID_number + "','" + list_name + "','" + list_area + "','" + list_edu_group + "','" + list_period + "','" + list_tel + "','" + list_email + "');");
            print('导入成功')
        except Exception as ErrorResult:
            print(ErrorResult)
            return '导入数据库异常'
