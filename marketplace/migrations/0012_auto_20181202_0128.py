# Generated by Django 2.0.5 on 2018-12-01 19:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0011_auto_20181202_0128'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='product',
        ),
        migrations.AddField(
            model_name='cart',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='marketplace.product'),
        ),
    ]
