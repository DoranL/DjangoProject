from django.db import models


# Create your models here.
class Genre(models.Model):
    class Meta:
        db_table = "genre"
    name = models.CharField(max_length=70, default='')


class Animation(models.Model):
    class Meta:
        db_table = "animations"
    title = models.CharField(max_length=70, default='')
    original_title = models.CharField(max_length=70, default='')
    genre = models.ManyToManyField(Genre, related_name='animations')
    company = models.CharField(max_length=70, default='')
    rated = models.CharField(max_length=70, default='')
    broadcasted_date = models.CharField(max_length=70, default='')
    chapters = models.CharField(max_length=70, default='')
    story = models.TextField(max_length=256, default='')
    img = models.TextField(max_length=256, default='')


class Game(models.Model):
    rank = models.IntegerField()
    appid = models.IntegerField()
    last_week_rank = models.IntegerField()
    peak_in_game = models.IntegerField()
    rollup_date = models.DateTimeField()

    def __str__(self):
        return f"Game #{self.rank}: {self.appid}"


class Question(models.Model):
    question_text = models.CharField(max_length=256)
    pub_date = models.DateTimeField(verbose_name="date published")

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)