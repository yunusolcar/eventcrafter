# Generated by Django 5.0.3 on 2024-03-10 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='event_date',
            field=models.DateTimeField(null=True),
        ),
    ]