# Generated by Django 2.2.4 on 2019-11-17 12:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Delivery', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restaurante',
            name='localizacao',
        ),
    ]