# Generated by Django 3.0.5 on 2020-04-22 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pdd', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pdd_upload',
            name='file',
            field=models.FileField(default='that good', upload_to=''),
        ),
    ]
