# Generated by Django 4.1.7 on 2023-03-09 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simple_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='address',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='students',
            name='first_name',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='students',
            name='last_name',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='students',
            name='mobile',
            field=models.IntegerField(),
        ),
    ]
