# Generated by Django 5.0.7 on 2024-08-20 23:36

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("agendamentos", "0005_remove_horario_intervalo_alter_horario_frequencia"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="agendamento",
            options={"ordering": ["-created_at"]},
        ),
        migrations.AddField(
            model_name="agendamento",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
    ]
