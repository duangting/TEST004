from rest_framework import serializers


#做model的映射
class serializers_Employee(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    name=serializers.CharField()
    email=serializers.EmailField()

