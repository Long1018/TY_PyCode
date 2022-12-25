from django.urls import path
from SchoolManage import views

urlpatterns = [
    path(r'list/', views.SLmanage),
    path(r'list/FileUpload/', views.FileUpload),
    # path(r'list/Filedownload/', views.FileDownload),

]
