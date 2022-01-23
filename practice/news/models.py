from django.db import models

class article(models.Model):
    title = models.CharField('Название', max_length=50, default='Статья')
    anons = models.CharField('Анонс', max_length=250, default='Анонс статьи!')
    full_text = models.TextField('Статья', default='Ничего нет')
    date = models.DateTimeField('Дата публикации')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/news/{self.id}'

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
