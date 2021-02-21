# Generated by Django 3.0.5 on 2021-02-21 11:02

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_auto_20210221_1145'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='created_add',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 21, 11, 2, 11, 607320, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='friendrequest',
            name='request_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 21, 11, 2, 11, 606317, tzinfo=utc)),
        ),
    ]