# Generated by Django 3.0.6 on 2020-05-31 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arts', '0009_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='address',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
        migrations.AddField(
            model_name='order',
            name='phone',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
    ]
