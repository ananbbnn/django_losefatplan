# Generated by Django 5.2 on 2025-06-06 08:49

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Plan Name')),
                ('private', models.BooleanField(default=False, verbose_name='Private Plan')),
                ('height', models.FloatField(default=0, verbose_name='Height')),
                ('weight', models.FloatField(default=0, verbose_name='Weight')),
                ('start_time', models.DateTimeField(auto_now_add=True, verbose_name='Start Time')),
                ('end_time', models.DateTimeField(auto_now_add=True, verbose_name='End Time')),
                ('month_target', models.FloatField(default=0, verbose_name='Monthly Target')),
                ('final_target', models.FloatField(default=0, verbose_name='Final Target')),
                ('description', models.TextField(blank=True, max_length=450, verbose_name='Description')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Plan',
                'verbose_name_plural': 'Plans',
            },
        ),
    ]
