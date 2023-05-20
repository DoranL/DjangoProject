from django.db import models

# Create your models here.
class Game(models.Model):
    id = models.IntegerField(primary_key=True, editable=True)
    name = models.CharField(max_length=100)
    release_date = models.DateField(null=True)
    price = models.FloatField(null=True)
    image = models.TextField(null=True)
    
    def __str__(self):
        return  self.name