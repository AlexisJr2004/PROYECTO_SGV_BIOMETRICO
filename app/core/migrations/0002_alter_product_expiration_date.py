# Generated by Django 4.2 on 2024-07-02 04:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='expiration_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 8, 1, 4, 13, 0, 877298, tzinfo=datetime.timezone.utc), verbose_name='Caducidad'),
        ),
    ]