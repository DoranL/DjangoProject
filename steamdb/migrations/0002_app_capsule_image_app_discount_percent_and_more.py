# Generated by Django 4.2.1 on 2023-06-05 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('steamdb', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='app',
            name='capsule_image',
            field=models.TextField(default="{% static 'header_image.jpg' %}"),
        ),
        migrations.AddField(
            model_name='app',
            name='discount_percent',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='app',
            name='final_price',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='app',
            name='header_image',
            field=models.TextField(default="{% static 'header_image.jpg' %}"),
        ),
        migrations.AddField(
            model_name='app',
            name='initial_price',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='app',
            name='is_free',
            field=models.BooleanField(null=True),
        ),
    ]