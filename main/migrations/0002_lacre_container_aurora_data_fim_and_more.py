# Generated by Django 5.0.6 on 2024-07-01 14:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lacre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(max_length=6, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='container_aurora',
            name='data_fim',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='container_aurora',
            name='data_inicio',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='container_aurora',
            name='fornecedor',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='carga',
            name='data_Lançamento_NF',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='carga',
            name='numero_DI',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='container',
            name='cavalo_saida',
            field=models.CharField(blank=True, max_length=8, null=True),
        ),
        migrations.AlterField(
            model_name='container',
            name='localização',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='main.localização'),
        ),
        migrations.AlterField(
            model_name='container',
            name='motorista_Saida',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='motorista_saida_set', to='main.motorista'),
        ),
        migrations.AlterField(
            model_name='container',
            name='prancha_saida',
            field=models.CharField(blank=True, max_length=8, null=True),
        ),
        migrations.AlterField(
            model_name='container',
            name='lacre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.lacre'),
        ),
    ]