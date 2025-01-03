from django.contrib.auth import get_user_model
from django.db import models
from django.conf import settings

# Чтобы создать таблицу в базе данных необходимо создать класс, который будет представлять собой модель
# Т.е модель - это определенная таблица в БД, с помощью модели мы можем управлять таблицей в БД

# Создание таблиц происходит в тот момент, когда мы создаем миграции;
# Миграция - синхронизация программы с БД
from django.db import models
from django.utils.timezone import now

class Tag(models.Model):
    name = models.CharField('Тег', max_length=50, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

class Artiles(models.Model):
    title = models.CharField('Название', max_length=50)
    anons = models.CharField('Анонс', max_length=250)
    full_text = models.TextField('Статья')
    date = models.DateTimeField('Дата публикации')
    image = models.ImageField('Изображение', upload_to='images/', blank=True, null=True)
    author = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, related_name='posts', null=True, default=None)
    tags = models.ManyToManyField(Tag, related_name='articles', blank=True, verbose_name='Теги')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/news/{self.id}'

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'


class Comment(models.Model):
    article = models.ForeignKey('Artiles', on_delete=models.CASCADE, related_name='comments', verbose_name='Статья')
    content = models.TextField('Комментарий')
    created_at = models.DateTimeField('Дата публикации', default=now)
    author = models.CharField('Автор', max_length=50)

    def __str__(self):
        return f'Комментарий от {self.author} к статье "{self.article.title}"'

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'