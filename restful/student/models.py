from django.db import models

# Create your models here.
class Student(models.Model):
    Student_id = models.CharField(max_length=10)
    Name = models.CharField(max_length=100)
    branch = models.CharField(max_length=100)

    def __str__(self):
        return self.Name