# Generated by Django 4.0 on 2021-12-15 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking_time', '0005_reservebooktime_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservebooktime',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, unique=True),
        ),
        migrations.AlterField(
            model_name='reservebooktime',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, unique=True),
        ),
    ]
