# Generated by Django 2.2.4 on 2019-11-17 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Delivery', '0003_auto_20191117_1509'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurante',
            name='dias',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
