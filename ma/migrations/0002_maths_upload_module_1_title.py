# Generated by Django 3.0.5 on 2020-04-27 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ma', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='maths_upload_module_1',
            name='Title',
            field=models.CharField(default='module 1', max_length=100),
        ),
    ]