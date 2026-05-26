from django.db import models

class Article(models.Model):
    title = models.CharField('Название', max_length=50)
    anons = models.CharField('Анонс', max_length=250)
    full_text = models.TextField('Статья')
    date = models.DateTimeField('Дата публикации')

    def __str__(self):
        return self.title

    # ВАЖНО: отступ как у def __str__ (4 пробела)
    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'