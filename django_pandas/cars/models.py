from django.db import models

BRAND_CHOICES = (
    ('MERCEDES','Mercedes'),
    ('TESLA','Tesla'),
    ('BMW','Bmw'),
    ('AUDI','Audi')
)
# Create your models here.
class Cars(models.Model):
    brand       = models.CharField(max_length=100,choices=BRAND_CHOICES)
    model       = models.CharField(max_length=200)
    max_speed   = models.PositiveIntegerField()
    country     = models.CharField(max_length=200,blank=True)
    added       = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return "{} - {}- {}".format(self.brand,self.model,self.country)

    # Override the save method
    def save(self,*args,**kwargs):
        if self.brand == 'TESLA':
            self.country = 'USA'
        else:
            self.country = 'Germany'
        super().save(*args,**kwargs)