# Generated by Django 4.2 on 2023-04-04 19:20

import datetime
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ponto',
            fields=[
                ('id_ponto', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('data_ponto', models.DateTimeField(default=datetime.datetime(2023, 4, 4, 16, 20, 29, 731522), editable=False)),
                ('id_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.usuarios')),
            ],
        ),
    ]
