# Generated by Django 5.0.6 on 2024-07-01 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_tipoavaria_remove_container_avaria_container_avaria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tipoavaria',
            name='nome',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
