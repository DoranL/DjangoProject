# Generated by Django 4.2.1 on 2023-05-26 19:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('steamdb', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rank',
            name='app',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='rank', to='steamdb.app'),
        ),
    ]