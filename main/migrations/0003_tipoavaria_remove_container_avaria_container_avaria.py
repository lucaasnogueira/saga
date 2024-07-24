# Generated by Django 5.0.6 on 2024-07-01 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_lacre_container_aurora_data_fim_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoAvaria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='container',
            name='avaria',
        ),
        migrations.AddField(
            model_name='container',
            name='avaria',
            field=models.ManyToManyField(blank=True, null=True, to='main.tipoavaria'),
        ),
    ]