from django.db import models
from django.contrib.auth.models import User

class Table(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, default=None)
    name = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.name} id:{self.id}"

class Subject(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, default=None)
    name = models.CharField(max_length=64)
    table = models.ForeignKey(Table, on_delete=models.CASCADE, related_name="subjectToTable")

    def __str__(self):
        return self.name

class Week(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, default=None)
    number = models.IntegerField()
    table = models.ForeignKey(Table, on_delete=models.CASCADE, related_name="weekToTable")

    def __str__(self):
        return f"Week {self.number}, {self.table}"

class Node(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, default=None)
    inactive = models.BooleanField(default=True)
    completed = models.BooleanField(default=False)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name="nodeSubject")
    week = models.ForeignKey(Week, on_delete=models.CASCADE, related_name="nodeWeek")

    def __str__(self):
        return f"{self.subject} Week {self.week.number}"
