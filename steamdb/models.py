from django.db import models


# Create your models here.
class Game(models.Model):
    id = models.IntegerField(primary_key=True, editable=True)
    name = models.CharField(max_length=100)
    release_date = models.DateField(null=True)
    price = models.FloatField(null=True)
    image = models.TextField(null=True)

    def __str__(self):
        return self.name


class Info(models.Model):
    rank = models.IntegerField(primary_key=True)
    appid = models.IntegerField()
    last_week_rank = models.IntegerField()
    peak_in_game = models.IntegerField()

    def __str__(self):
        return str(self.rank)

    class Meta:
        db_table = 'steamdb_gameinfo'


class GameName(models.Model):
    appid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'steamdb_getname'
