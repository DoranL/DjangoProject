# Generated by Django 4.2.2 on 2023-06-18 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('steamdb', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='app',
            name='capsule_image',
            field=models.TextField(default="{% static 'header_image.jpg' %}", null=True),
        ),
        migrations.AlterField(
            model_name='app',
            name='header_image',
            field=models.TextField(default="{% static 'header_image.jpg' %}", null=True),
        ),
    ]
