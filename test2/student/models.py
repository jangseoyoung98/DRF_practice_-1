from django.db import models

class Student(models.Model) :
    #1. unique=True -> 해당 필드의 값이 겹치지 않게 하는 조건
    student_id = models.CharField(max_length=15, unique=True)
    name = models.CharField(max_length=30)
    age = models.IntegerField()

    def __str__(self):
        return self.name
