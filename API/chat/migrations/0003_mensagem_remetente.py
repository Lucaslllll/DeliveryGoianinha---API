# Generated by Django 2.2.4 on 2019-11-17 22:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_remetente'),
    ]

    operations = [
        migrations.AddField(
            model_name='mensagem',
            name='remetente',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='chat.Remetente'),
        ),
    ]