from django.db import models


# Create your models here.
class App(models.Model):
    class Meta:
        db_table = "app"

    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)


class Rank(models.Model):
    class Meta:
        db_table = "rank"

    app = models.OneToOneField(App, on_delete=models.SET_NULL, null=True, related_name='rank')
    rank = models.IntegerField(primary_key=True)
    last_week_rank = models.IntegerField()
    peak_in_game = models.IntegerField()
