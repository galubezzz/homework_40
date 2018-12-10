from django.db import models

# Create your models here.

class Task(models.Model):
    name = models.CharField(max_length=75, blank=False, null=False, verbose_name="Задача")
    description = models.TextField(max_length=1000, blank=True, null=True, verbose_name="Описание")
    status = models.CharField(max_length=20, blank=False, null=False, default="new", verbose_name="Статус")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"