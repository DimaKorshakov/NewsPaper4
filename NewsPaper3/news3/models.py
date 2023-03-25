from django.db import models


class News(models.Model):
    date = models.DateField(auto_now_add=True)
    header = models.CharField(max_length=50, unique=True)
    description = models.TextField(unique=True)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f'{self.date} {self.header} {self.description[:20]} {self.email}'

    def get_absolute_url(self):
        return f'/newses/{self.id}'
