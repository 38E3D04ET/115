from django.db import models


class Post(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField()
    date = models.DateTimeField()
    category = models.ForeignKey('category', on_delete=models.CASCADE)
    source = models.ForeignKey('source', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} {self.date}'

    def get_absolute_url(self):  # добавим абсолютный путь, чтобы после создания нас перебрасывало на страницу с товаром
        return f'/posts/{self.id}'

class Category(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return f'{self.name}'

class Source(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return f'{self.name}'

