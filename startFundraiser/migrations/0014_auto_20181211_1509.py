# Generated by Django 2.0.5 on 2018-12-11 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('startFundraiser', '0013_auto_20181211_1427'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='body',
        ),
        migrations.RemoveField(
            model_name='post',
            name='description2',
        ),
        migrations.RemoveField(
            model_name='post',
            name='order',
        ),
        migrations.RemoveField(
            model_name='post',
            name='slug',
        ),
        migrations.AddField(
            model_name='post',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
