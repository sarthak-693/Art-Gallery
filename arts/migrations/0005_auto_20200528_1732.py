# Generated by Django 3.0.6 on 2020-05-28 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arts', '0004_auto_20200528_1430'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
    ]