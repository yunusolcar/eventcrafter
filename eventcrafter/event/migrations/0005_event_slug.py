# Generated by Django 5.0.3 on 2024-03-11 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0004_event_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
    ]
