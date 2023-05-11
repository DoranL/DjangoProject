import json
from django.db import models


class Rank(models.Model):
    rollup_date = models.IntegerField()
    rank = models.IntegerField()
    appid = models.IntegerField()
    last_week_rank = models.IntegerField()
    peak_in_game = models.IntegerField()


with open('gameDb.json') as f:
    data = json.load(f)


for rank_data in data['response']['ranks']:
    Rank.objects.create(
        rollup_date=data['response']['rollup_date'],
        rank=rank_data['rank'],
        appid=rank_data['appid'],
        last_week_rank=rank_data['last_week_rank'],
        peak_in_game=rank_data['peak_in_game']
    )