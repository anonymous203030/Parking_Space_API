# Generated by Django 4.0 on 2021-12-15 22:56

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking_time', '0007_alter_booktime_options_alter_reservebooktime_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booktime',
            name='floor',
            field=models.IntegerField(default=-1, validators=[django.core.validators.MaxValueValidator(1), django.core.validators.MinValueValidator(-5)]),
        ),
    ]
