import requests
from django.http import HttpResponse
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.pagination import PageNumberPagination
from django.views import View

from .models import Employee
from .serializers import serializers_Employee
from .serializers import serializers_Employee001
from rest_framework import mixins

from rest_framework import viewsets


# CBV模式

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    page_query_param = 'pg'
    max_page_size = 1000


class employee_viewsets(mixins.RetrieveModelMixin,
                        mixins.ListModelMixin, viewsets.GenericViewSet,
                        mixins.CreateModelMixin,
                        ):
    queryset = Employee.objects.all()
    serializer_class = serializers_Employee
    pagination_class = StandardResultsSetPagination


class employee_viewset001(viewsets.GenericViewSet,
                          mixins.ListModelMixin,
                          mixins.CreateModelMixin
                          ):
    queryset = Employee.objects.all()
    serializer_class = serializers_Employee
    pagination_class = StandardResultsSetPagination
    #pagination_class = StandardResultsSetPagination
    # 使用过滤器
    filter_backends = (DjangoFilterBackend,)
    # 定义需要使用过滤器的字段
    filter_fields = ('email', 'name')
    # fields='__all__'

class employee001_viewset(viewsets.GenericViewSet,
                          mixins.ListModelMixin,
                          mixins.CreateModelMixin
                          ):
    queryset = Employee.objects.all()
    serializer_class = serializers_Employee001
    pagination_class = StandardResultsSetPagination
    # 使用过滤器
    filter_backends = (DjangoFilterBackend,)
    # 定义需要使用过滤器的字段
    filter_fields = ('email',)





# class employee_view(
# ListAPIView,
# CreateAPIView,
#     # mixins.ListModelMixin,
#     # mixins.CreateModelMixin,
#     # generics.GenericAPIView
#                         ):
#
#     queryset = Employee.objects.all()
#     serializer_class = serializers_Employee
#     pagination_class = StandardResultsSetPagination
# def get(self, request, *args, **kwargs):
#     return self.list(request, *args, **kwargs) #需要使用restframeword的Response
#
# def post(self, request, *args, **kwargs):
#     return self.create(request, *args, **kwargs)
# def post(self,request):
#     serializer=serializers_Employee(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         print(serializer.data)
#         return  Response({"msg":"请求成功",'code':'201'},status=status.HTTP_200_OK)
#     return Response(serializer.error_messages,status=status.HTTP_404_NOT_FOUND)
