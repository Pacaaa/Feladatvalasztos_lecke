# Generated by Django 3.2.13 on 2022-04-22 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APP', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feladat',
            name='id',
        ),
        migrations.AlterField(
            model_name='feladat',
            name='nev',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
    ]