# Generated by Django 5.2 on 2025-06-06 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plan', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plan',
            name='end_time',
            field=models.DateTimeField(verbose_name='End Time'),
        ),
        migrations.AlterField(
            model_name='plan',
            name='start_time',
            field=models.DateTimeField(verbose_name='Start Time'),
        ),
    ]
