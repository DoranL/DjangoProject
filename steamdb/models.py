from django.contrib.humanize.templatetags.humanize import intcomma
from django.db import models


# Create your models here.
class App(models.Model):
    class Meta:
        db_table = "app"

    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    type = models.CharField(null=True, max_length=10)
    short_description = models.CharField(null=True, max_length=130)
    header_image = models.TextField(default="{% static 'header_image.jpg' %}", null=True)
    capsule_image = models.TextField(default="{% static 'header_image.jpg' %}", null=True)
    is_free = models.BooleanField(null=True)
    initial_price = models.IntegerField(null=True)
    discount_percent = models.IntegerField(null=True)
    final_price = models.IntegerField(null=True)


class Rank(models.Model):
    class Meta:
        db_table = "rank"

    app = models.OneToOneField(App, on_delete=models.SET_NULL, null=True, related_name='rank')
    rank = models.IntegerField(primary_key=True)
    last_week_rank = models.IntegerField()
    peak_in_game = models.IntegerField()
