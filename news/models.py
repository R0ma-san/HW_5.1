from django.db import models

class News(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    body = models.TextField(verbose_name='Текст')
    creation_date = models.DateTimeField(auto_now=True)
    editor_name = models.CharField(max_length=55, verbose_name='Автор новости', default=False)

    def __str__(self):
        return self.title