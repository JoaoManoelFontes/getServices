# Generated by Django 5.0.7 on 2024-08-20 12:21

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("usuarios", "0005_baseuser_profile_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="profissional",
            name="descricao",
            field=models.TextField(default=""),
            preserve_default=False,
        ),
    ]
