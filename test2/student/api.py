from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *

class StudentList(APIView):
    
    # 전체 다 보여지는 것
    def get(self, request):
        model = Student.objects.all()
        #3. many=True -> 다수의 데이터 queryset 형태를 serialize화 하고자 할 때 사용
        serializer = StudentSerializer(model, many=True)
        return Response(serializer.data)
    
    # 전체 리스트업에다가 추가로 post 하는 기능 생성
    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StudentDetail(APIView):

    # 특정 데이터만 보는 것
    def get(self, request, student_id):
        model = Student.objects.get(student_id=student_id)
        serializer = StudentSerializer(model)
        return Response(serializer.data)
    
    # 특정 데이터의 내용을 수정하는 것
    def put(self, request, student_id):
        model = Student.objects.get(student_id=student_id)

        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    # 특정 데이터를 삭제하는 것
    def delete(self, request, student_id):
        model = Student.objects.get(student_id=student_id)
        model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)