# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.


# -*- coding: utf-8 -*-


from django.db import models


class DataUser(models.Model):
    id = models.BigAutoField(primary_key=True)
    usertype = models.CharField(max_length=20, blank=True, null=True)
    username = models.CharField(max_length=50, blank=True, null=True)
    password = models.CharField(max_length=32, blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    role_id = models.BigIntegerField(blank=True, null=True)
    parent_id = models.BigIntegerField(blank=True, null=True)
    department = models.CharField(max_length=200, blank=True, null=True)
    id_card = models.CharField(max_length=20, blank=True, null=True)
    mail = models.CharField(max_length=20, blank=True, null=True)
    working_years = models.PositiveIntegerField()
    job_title = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    login_ip = models.CharField(max_length=255, blank=True, null=True)
    login_at = models.CharField(max_length=20, blank=True, null=True)
    login_num = models.BigIntegerField(blank=True, null=True)
    note = models.CharField(max_length=255, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    sort = models.BigIntegerField(blank=True, null=True)
    is_deleted = models.IntegerField(blank=True, null=True)
    create_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'data_user'


