from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import User


class Photos(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='files/photos')
    category = ArrayField(models.CharField(max_length=250), blank=True)
    description = models.CharField(max_length=450, blank=True)
    rating = models.DecimalField(max_digits=2, decimal_places=1, default=0.0,  blank=True)
    year_photo = models.PositiveSmallIntegerField(blank=True)

    def __str__(self):
        return self.name

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    photo = models.ForeignKey(Photos, on_delete=models.CASCADE)
    content = models.TextField(blank=True)

    def __str__(self) -> str:
        return self.user.username

