"""test004 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from employee.views import employee_viewset001,employee_viewsets,employee001_viewset
from apps.employee import view_base
# 创建路由器并注册我们的视图。
router = DefaultRouter()
router.register(r'index', employee_viewsets)
router.register(r'index001', employee_viewset001)
router.register('indes',employee001_viewset)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('logout/',view_base.test001),
    # path('index001/',employee_viewset001.as_view())
]
