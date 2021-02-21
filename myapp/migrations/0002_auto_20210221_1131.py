# Generated by Django 3.0.5 on 2021-02-21 09:31

import datetime
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friendrequest',
            name='request_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 21, 9, 31, 48, 648828, tzinfo=utc)),
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, validators=[django.core.validators.MaxLengthValidator(255, 'post title must be less than 255 character .')])),
                ('content', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='myapp.User')),
            ],
        ),
    ]
