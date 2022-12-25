# Create your views here.

# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from SchoolManage.models import SckoolManageSql
from django.shortcuts import render
from django.http import JsonResponse
import os, xlrd, math


def SLmanage(request):
    # 接收请求
    num = request.GET.get("num", 1)
    # 查询
    num = int(num)
    mvs = page(num)
    pre_page = num - 1
    next_page = num + 1

    return render(request, 'index2.html', {'movies': mvs, 'pre_page': pre_page, 'next_page': next_page})

    # select_DB = list(SckoolManageSql.objects.all()[:20].values('id', 'name', 'period', 'area', 'edu_group', 'create_at'))
    # result = {'responseCode': 0, 'responseMsg': '查询成功', 'data': select_DB}

    return JsonResponse(result, safe=False, json_dumps_params={'ensure_ascii': False})


# 首页分页
def page(number, size=20):
    number = int(number)
    # 判断页码
    if number < 1:
        number = 1
    # 总的页数
    total_records = SckoolManageSql.objects.count()
    total_page = int(math.ceil(total_records * 1.0 / size))
    if number > total_page:
        number = total_page
    # 获取当前页码数据
    mvs = list(SckoolManageSql.objects.all()[((number - 1) * size):(number * size)].values('id', 'name', 'period', 'area',                                                                         'edu_group', 'create_at'))
    return mvs


# 首页文件上传
def FileUpload(request):
    # 创建文件夹
    if not os.path.exists('Files'):
        os.makedirs('Files')
    # 接收请求参数：
    if request.method == 'GET':
        return render(request, 'index.html')
    elif request.method == 'POST':
        n_file = request.FILES.get('FileName', '')
        FilePath = os.path.join(os.getcwd(), 'Files', n_file.name)
        with open(FilePath, 'wb')as fw:
            # fw.write(n_file.read())
            for n_data in n_file.chunks():
                fw.write(n_data)
            excel_result = ManageExcel(n_file.name)
            if excel_result == "文件格式错误":
                result = {'responseCode': 2, 'responseMsg': '导入失败', 'data': '导入学校信息的Excel文件格式错误，请下载学校信息Excel模板按格式上传'}
                return JsonResponse(result, safe=False, json_dumps_params={'ensure_ascii': False})
            elif excel_result == "空文件":
                result = {'responseCode': 3, 'responseMsg': '导入失败', 'data': "导入学校信息的Excel文件为空文件，请补充数据"}
                return JsonResponse(result, safe=False, json_dumps_params={'ensure_ascii': False})
            elif excel_result == "上传异常":
                result = {'responseCode': 4, 'responseMsg': '导入失败', 'data': "导入学校信息的Excel文件时过程异常"}
                return JsonResponse(result, safe=False, json_dumps_params={'ensure_ascii': False})
            elif excel_result == "导入数据库异常":
                result = {'responseCode': 5, 'responseMsg': '导入失败', 'data': "学校信息的Excel文件导入数据库异常"}
                return JsonResponse(result, safe=False, json_dumps_params={'ensure_ascii': False})
            else:
                result = {'responseCode': 1, 'responseMsg': '导入成功', 'data': "导入学校信息的Excel文件成功"}
                return JsonResponse(result, safe=False, json_dumps_params={'ensure_ascii': False})
    else:
        result = {'responseCode': 6, 'responseMsg': '导入失败', 'data': "导入学校信息Excel文件时后台接收异常"}
        return JsonResponse(result, safe=False, json_dumps_params={'ensure_ascii': False})


# 处理导入excel
def ManageExcel(n_value):
    # 获取excel
    path = os.path.abspath('.') + '//' + 'Files'
    n_path = path + '//' + n_value
    namelist = os.listdir(path)
    for i in namelist:
        if os.path.isfile(n_path) and i == n_value:
            wb = xlrd.open_workbook(n_path)
            sheet = wb.sheet_by_index(0)
            headline = sheet.row_values(0)
            n_headline = str(headline[0])
            Hs = sheet.nrows
            try:
                if n_headline != "学校名称":
                    return '文件格式错误'
                elif Hs < 2:
                    return '空文件'
                else:
                    ShoolData = []
                    counts = 1
                    while counts < Hs:
                        row = sheet.row_values(counts)
                        counts += 1
                        ShoolData.append(row)
                    try:
                        # 关联账号标志 ID_number      #--------------------------------注意传值------------
                        ID_number = 1
                        Save_result = SckoolManageSql.SaveDataBase(ShoolData, ID_number)
                        if Save_result == '导入数据库异常':
                            return ('导入数据库异常')
                    except Exception as ErrorResult:
                        print(ErrorResult)
                        return ('导入数据库异常')
                        # return '导入数据成功'
            except Exception as ErrorResult:
                print(ErrorResult)
                return '上传异常'
        else:
            continue


# 首页文件下载
def FileDownload(request):
    # 创建模板文件夹
    # 模板路径 .Pytese/ExampleFiles
    if not os.path.exists('ExampleFiles'):
        os.makedirs('ExampleFiles')
    else:
        pass
