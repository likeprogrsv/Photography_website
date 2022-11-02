from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import User


class Table_test(models.Model):
    title = models.CharField('Name', max_length=80)
    decription = models.TextField('Description')

    def __str__(self):
        return self.title


class Photos(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='files/photos')
    category = ArrayField(models.CharField(max_length=250), blank=True)
    description = models.CharField(max_length=450, blank=True)
    rating = models.DecimalField(max_digits=2, decimal_places=1, default=0.0,  blank=True)
    year_photo = models.PositiveSmallIntegerField(blank=True)

    def __str__(self):
        return self.name


class Comments(models.Model):
    # user = models.ForeignKey(User,null=True,blank=True,on_delete=models.CASCADE)
    photo = models.ForeignKey(Photos, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return f'Photo name: {self.photo.name}. Username: {self.name}'


