"""wx_test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls import url, include
from django.views.static import serve
from django.conf import settings
from index import views

urlpatterns = [
    # 设置首页
    path('', views.index),
    # 设置admin
    url(r'^admin/', admin.site.urls),
    # 问诊
    url('^', include('eyetest.urls')),
    # 影像&数据库
    url('^', include('getim.urls')),
    # 治疗
    url('^', include('advice.urls')),
    ##media配置——配合settings中的MEDIA_ROOT的配置，就可以在浏览器的地址栏访问media文件夹及里面的文件了
    re_path(r'media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT})
]
