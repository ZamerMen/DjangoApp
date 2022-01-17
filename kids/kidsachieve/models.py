from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify
from time import time

from django.contrib.auth import get_user_model
User = get_user_model()


def gen_slug(s):
    return slugify(s, allow_unicode=True)


class Child(models.Model):
    first_name = models.CharField(max_length=50, db_index=True)
    nick_name = models.CharField(max_length=50, db_index=True, unique=True)
    age = models.IntegerField()
    slug = models.SlugField(max_length=50, unique=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'child - {self.first_name} {self.nick_name}'

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.nick_name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('child_detail_url', kwargs={'slug': self.slug})

    def get_update_url(self):
        return reverse('child_update_url', kwargs={'slug': self.slug})

    def get_delete_url(self):
        return reverse('child_delete_url', kwargs={'slug': self.slug})


class Work(models.Model):
    title = models.CharField(max_length=50)
    point = models.IntegerField(default=10)
    comment = models.CharField(max_length=150, blank=True)
    slug = models.SlugField(max_length=50, unique=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'work - {self.title}'

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title + ' ' + str(self.user))
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('work_detail_url', kwargs={'slug': self.slug})

    def get_update_url(self):
        return reverse('work_update_url', kwargs={'slug': self.slug})

    def get_delete_url(self):
        return reverse('work_delete_url', kwargs={'slug': self.slug})


class Achievement(models.Model):
    child_nick = models.ForeignKey(Child, on_delete=models.CASCADE, null=True)
    work_title = models.ForeignKey(Work, on_delete=models.CASCADE, null=True)
    comment = models.CharField(max_length=150, blank=True)
    date_done = models.DateTimeField(auto_now_add=True)
    benefit_point = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=50, unique=True, blank=True)

    def __str__(self):
        return f'{self.child_nick} done the {self.work_title}'

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = self.child_nick.slug + '-' + self.work_title.slug + str(int(time()))
        super().save(*args, **kwargs)

    def get_update_url(self):
        return reverse('achievement_update_url', kwargs={'slug': self.slug})

    def get_delete_url(self):
        return reverse('achievement_delete_url', kwargs={'slug': self.slug})