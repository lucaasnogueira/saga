# Generated by Django 5.0.6 on 2024-07-02 13:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_avariacarga_remove_carga_avaria_carga_avaria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carga',
            name='container_saida',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='carga_saida_set', to='main.container'),
        ),
    ]
