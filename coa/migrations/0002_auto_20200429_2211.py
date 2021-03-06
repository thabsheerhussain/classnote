# Generated by Django 3.0.5 on 2020-04-29 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coa', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='coa_upload_module_1',
            name='Title',
            field=models.CharField(default='enter subject', max_length=100),
        ),
        migrations.AddField(
            model_name='coa_upload_module_2',
            name='Title',
            field=models.CharField(default='enter subject', max_length=100),
        ),
        migrations.AddField(
            model_name='coa_upload_module_3',
            name='Title',
            field=models.CharField(default='enter subject', max_length=100),
        ),
        migrations.AddField(
            model_name='coa_upload_module_4',
            name='Title',
            field=models.CharField(default='enter subject', max_length=100),
        ),
        migrations.AddField(
            model_name='coa_upload_module_5',
            name='Title',
            field=models.CharField(default='enter subject', max_length=100),
        ),
        migrations.AddField(
            model_name='coa_upload_module_6',
            name='Title',
            field=models.CharField(default='enter subject', max_length=100),
        ),
        migrations.AlterField(
            model_name='coa_upload_module_1',
            name='File',
            field=models.FileField(upload_to='coa/module1'),
        ),
        migrations.AlterField(
            model_name='coa_upload_module_2',
            name='File',
            field=models.FileField(upload_to='coa/module2'),
        ),
        migrations.AlterField(
            model_name='coa_upload_module_3',
            name='File',
            field=models.FileField(upload_to='coa/module2'),
        ),
        migrations.AlterField(
            model_name='coa_upload_module_4',
            name='File',
            field=models.FileField(upload_to='coa/module2'),
        ),
        migrations.AlterField(
            model_name='coa_upload_module_5',
            name='File',
            field=models.FileField(upload_to='coa/module2'),
        ),
        migrations.AlterField(
            model_name='coa_upload_module_6',
            name='File',
            field=models.FileField(upload_to='coa/module2'),
        ),
    ]
