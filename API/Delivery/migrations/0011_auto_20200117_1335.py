# Generated by Django 2.2.4 on 2020-01-17 15:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Delivery', '0010_comida_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurante',
            name='cor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Delivery.Cor'),
        ),
    ]
