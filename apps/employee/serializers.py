from rest_framework import serializers
from .models import Employee

#做model的映射
class serializers_Employee(serializers.ModelSerializer):
    # id=serializers.IntegerField(read_only=True)
    # name=serializers.CharField()
    # email=serializers.EmailField()
    #
    # #重写create方法
    # def create(self, validated_data):
    #     return Employee.objects.create(**validated_data)
    class Meta:
        model=Employee
        fields=('__all__')

class serializers_Employee001(serializers.ModelSerializer):
    class Meta:
        model=Employee
        fields=('email',)
