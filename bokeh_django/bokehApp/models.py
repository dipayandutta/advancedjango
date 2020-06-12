from django.db import models

# Create your models here.
class Products(models.Model):

    COLOR = (
        ("WHITE","white"),
        ("BLUE","Blue"),
        ("BLACK","Black"),
        ("GREEN","Green"),
    )

    name = models.CharField(max_length=100)
    color = models.CharField(max_length=100,choices=COLOR)
    price = models.IntegerField()


    def __str__(self):
        return '{} - {}'.format(self.name,self.color)