# Generated by Django 5.0.7 on 2024-08-13 22:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agendamentos', '0002_agendamento_status'),
        ('usuarios', '0003_alter_profissional_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='horario',
            name='profissional',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='usuarios.profissional'),
            preserve_default=False,
        ),
    ]
