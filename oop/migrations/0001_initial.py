# Generated by Django 3.0.5 on 2020-04-22 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='oop_upload_module_1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Module', models.CharField(max_length=50)),
                ('File', models.FileField(default='that good', upload_to='')),
                ('Description', models.TextField()),
                ('Email', models.CharField(default='that good', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='oop_upload_module_2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Module', models.CharField(max_length=50)),
                ('File', models.FileField(default='that good', upload_to='')),
                ('Description', models.TextField()),
                ('Email', models.CharField(default='that good', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='oop_upload_module_3',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Module', models.CharField(max_length=50)),
                ('File', models.FileField(default='that good', upload_to='')),
                ('Description', models.TextField()),
                ('Email', models.CharField(default='that good', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='oop_upload_module_4',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Module', models.CharField(max_length=50)),
                ('File', models.FileField(default='that good', upload_to='')),
                ('Description', models.TextField()),
                ('Email', models.CharField(default='that good', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='oop_upload_module_5',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Module', models.CharField(max_length=50)),
                ('File', models.FileField(default='that good', upload_to='')),
                ('Description', models.TextField()),
                ('Email', models.CharField(default='that good', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='oop_upload_module_6',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Module', models.CharField(max_length=50)),
                ('File', models.FileField(default='that good', upload_to='')),
                ('Description', models.TextField()),
                ('Email', models.CharField(default='that good', max_length=50)),
            ],
        ),
    ]
