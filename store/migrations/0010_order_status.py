# Generated by Django 3.2.5 on 2021-07-18 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_alter_order_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]