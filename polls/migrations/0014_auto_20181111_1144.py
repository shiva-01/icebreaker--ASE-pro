# Generated by Django 2.1.1 on 2018-11-11 06:14

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0013_auto_20181110_1734'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 11, 11, 6, 13, 59, 978089, tzinfo=utc), null=True),
        ),
    ]
