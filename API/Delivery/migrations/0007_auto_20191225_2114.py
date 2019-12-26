# Generated by Django 2.2.4 on 2019-12-25 23:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Delivery', '0006_auto_20191130_1349'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='codimentos',
            name='preco',
        ),
        migrations.AddField(
            model_name='codimentos',
            name='restaurante',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Delivery.Restaurante'),
        ),
    ]
