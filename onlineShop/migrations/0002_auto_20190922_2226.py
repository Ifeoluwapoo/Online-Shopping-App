# Generated by Django 2.2.1 on 2019-09-22 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlineShop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='phoneNumber',
            field=models.PositiveIntegerField(blank=True, max_length=15, null=True),
        ),
    ]