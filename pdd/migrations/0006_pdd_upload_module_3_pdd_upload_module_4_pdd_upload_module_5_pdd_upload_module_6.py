# Generated by Django 3.0.5 on 2020-04-22 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pdd', '0005_auto_20200422_2120'),
    ]

    operations = [
        migrations.CreateModel(
            name='pdd_upload_module_3',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Module', models.CharField(max_length=50)),
                ('File', models.FileField(default='that good', upload_to='')),
                ('Description', models.TextField()),
                ('Email', models.CharField(default='that good', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='pdd_upload_module_4',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Module', models.CharField(max_length=50)),
                ('File', models.FileField(default='that good', upload_to='')),
                ('Description', models.TextField()),
                ('Email', models.CharField(default='that good', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='pdd_upload_module_5',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Module', models.CharField(max_length=50)),
                ('File', models.FileField(default='that good', upload_to='')),
                ('Description', models.TextField()),
                ('Email', models.CharField(default='that good', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='pdd_upload_module_6',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Module', models.CharField(max_length=50)),
                ('File', models.FileField(default='that good', upload_to='')),
                ('Description', models.TextField()),
                ('Email', models.CharField(default='that good', max_length=50)),
            ],
        ),
    ]
