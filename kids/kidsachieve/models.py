from django.db import models
from django.shortcuts import reverse


class Child(models.Model):
    first_name = models.CharField(max_length=50, db_index=True)
    nick_name = models.CharField(max_length=50, db_index=True, unique=True)
    age = models.IntegerField()

    def __str__(self):
        return f'child {self.first_name} {self.last_name}'


class Work(models.Model):
    title = models.CharField(max_length=50, unique=True)
    points = models.IntegerField()
    comments = models.CharField(max_length=150)

    def __str__(self):
        return f'work: {self.title}'


class AchieveList(models.Model):
    child_id = models.ManyToManyField('Child', related_name='achievement')
    work_id = models.ManyToManyField('Work', related_name='work')
    date_done = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'child{Child.objects.get(id__exact=self.child_id)}'