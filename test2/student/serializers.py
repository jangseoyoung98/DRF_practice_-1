from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer) :

    student_id = serializers.CharField(required=False)
    name = serializers.CharField(required=False)
    age = serializers.IntegerField(required=False)

    class Meta:
        model = Student
        fields = '__all__'
    #2. Meta 클래스 (https://www.delftstack.com/ko/howto/django/class-meta-in-django/)
    #   다른 데이터에 대한 정보를 제공하는 특정 데이터 집합. 모델 자체에 대한 데이터를 추가해야 하는 경우 사용
