# Generated by Django 3.1.7 on 2021-03-09 07:12

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('cbv', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='last_accessed',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 9, 7, 12, 4, 635379, tzinfo=utc)),
        ),
    ]
