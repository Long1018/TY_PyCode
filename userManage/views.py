# -*- coding: utf-8 -*-
import json

from django.http import JsonResponse, HttpResponse
from userManage.models import DataUser


# Create your views here.


# 用户登录
def UserLogin(request):
    LgName = request.POST.get('LgName', '')
    LgPassWord = request.POST.get('LgPassWord', '')
    if request.method == "GET":
        result = {'responseCode': 0, 'responseMsg': '登录失败', 'data': '登录失败'}
        return JsonResponse(result, safe=False, json_dumps_params={'ensure_ascii': False})
    else:
        try:
            LoginData = DataUser.objects.filter(username=LgName, password=LgPassWord)
            if LoginData and LoginData != []:
                for dt in LoginData:
                    print(dt.username, dt.password)
                return HttpResponse('用户' + str(dt.username) + '登录成功')
            else:
                return HttpResponse('账户名或密码错误')
        except Exception as ER:
            print(ER)
            return HttpResponse('登录失败')


# 用户注册
def UserRegister(request):
    if request.method == "GET":
        result = {'responseCode': 0, 'responseMsg': '注册失败', 'data': '注册失败'}
        return JsonResponse(result, safe=False, json_dumps_params={'ensure_ascii': False})
    else:
        # 接收
        IdName = request.POST.get('IDname', '')
        PassWord = request.POST.get('PassWord', '')
        # 查重
        UserRegisterData = DataUser.objects.filter(username=IdName, password=PassWord)
        if UserRegisterData:
            return HttpResponse('用户重复,修改用户名或密码')
        else:
            if IdName and PassWord:
                stu = DataUser(username=IdName, password=PassWord, working_years='0')
                stu.save()
                result = {'responseCode': 0, 'responseMsg': '注册成功', 'data': '注册成功'}
                return JsonResponse(result, safe=False, json_dumps_params={'ensure_ascii': False})
            else:
                result = {'responseCode': 0, 'responseMsg': '注册失败', 'data': '名称或密码为空，注册失败'}
                return JsonResponse(result, safe=False, json_dumps_params={'ensure_ascii': False})
# 账号列表

