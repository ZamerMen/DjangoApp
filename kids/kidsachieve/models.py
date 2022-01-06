from django.db import models
from django.shortcuts import reverse


class Child(models.Model):
    first_name = models.CharField(max_length=50, db_index=True)
    nick_name = models.CharField(max_length=50, db_index=True, unique=True)
    age = models.IntegerField()

    def __str__(self):
        return f'child - {self.first_name} {self.nick_name}'


class Work(models.Model):
    title = models.CharField(max_length=50, unique=True)
    points = models.IntegerField(default=10)
    comments = models.CharField(max_length=150, blank=True)

    def __str__(self):
        return f'work - {self.title}'


class AchieveList(models.Model):
    child_nick = models.ForeignKey(Child, on_delete=models.CASCADE, null=True)
    work_title = models.ForeignKey(Work, on_delete=models.CASCADE, null=True)
    comments = models.CharField(max_length=150, blank=True)
    correct_point = models.IntegerField(default=0)
    date_done = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.child_nick} done the {self.work_title}'
