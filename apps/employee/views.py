from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Employee
from .serializers import serializers_Employee
#CBV模式
class employee_view(APIView):
    def get(self,request):
        all_employee=Employee.objects.all()
        ser=serializers_Employee(all_employee,many=True)

        return Response(ser.data) #需要使用restframeword的Response

    def post(self,request):
        serializer=serializers_Employee(data=request.data)
        if serializer.is_valid():
            serializer.save()
            print(serializer.data)
            return  Response({"msg":"请求成功",'code':'201'},status=status.HTTP_200_OK)
        return Response(serializer.error_messages,status=status.HTTP_404_NOT_FOUND)


