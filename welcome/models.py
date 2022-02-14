from django.db import models

# Create your models here.

class PageView(models.Model):
    hostname = models.CharField(max_length=32)
    timestamp = models.DateTimeField(auto_now_add=True)

class Task(models.Model):
    title = models.CharField('Название', max_length=50)
    task = models.TextField('Описание')
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

