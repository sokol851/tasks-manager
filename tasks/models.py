from django.db import models


class Task(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name='название задачи'
    )
    is_completed = models.BooleanField(
        default=False,
        verbose_name='статус выполнения задачи',
    )

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

    def __str__(self):
        return self.title
