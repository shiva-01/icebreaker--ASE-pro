# Generated by Django 2.0.6 on 2018-12-01 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0002_auto_20181117_1700'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='cost',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='quantity',
            field=models.IntegerField(null=True),
        ),
    ]
