# avs_attendance_app/models.py
from django.db import models

class Student(models.Model):
    reg_no = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    
    

    def __str__(self):
        return f"{self.first_name} {self.last_name}"