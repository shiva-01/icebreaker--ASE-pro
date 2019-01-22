# Generated by Django 2.0.5 on 2018-11-17 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Testimony',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=120)),
                ('to_name', models.CharField(blank=True, max_length=120)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updates', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
