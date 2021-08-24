from django.db import models

class Question(models.Model):
    first_name = models.CharField(max_length=100, verbose_name='Имя')
    email = models.EmailField(verbose_name='Почта')
    question = models.TextField(verbose_name='Вопрос', default=False)
    is_unswerd = models.BooleanField(default=True, verbose_name='Ответил?')

    def __str__(self):
        return self.first_name