# Generated by Django 2.2.4 on 2019-11-17 20:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Delivery', '0005_auto_20191117_1813'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mensagem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mensagem', models.CharField(max_length=1200)),
                ('hora_envio', models.DateTimeField(auto_now_add=True)),
                ('lida', models.BooleanField(default=False)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sender', to=settings.AUTH_USER_MODEL)),
                ('restaurante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receiver', to='Delivery.Restaurante')),
            ],
            options={
                'ordering': ('hora_envio',),
            },
        ),
    ]
