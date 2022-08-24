from django.contrib import admin
from django.urls import path
from student.api import StudentList, StudentDetail
from rest_framework.authtoken import views

urlpatterns = [
    path('admin/', admin.site.urls),
    #4. as_view() -> 메소드에서 클래스의 인스턴스를 생성
    path('api/student_list', StudentList.as_view(), name='student_list'),
    path('api/student_list/<int:student_id>', StudentDetail.as_view(), name='student_detail'),
    path('api/auth', views.obtain_auth_token, name='user_auth-create'),
]
