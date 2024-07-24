# Generated by Django 5.0.6 on 2024-07-02 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_rename_nome_tipoavaria_avaria'),
    ]

    operations = [
        migrations.CreateModel(
            name='AvariaCarga',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avaria', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='carga',
            name='avaria',
        ),
        migrations.AddField(
            model_name='carga',
            name='avaria',
            field=models.ManyToManyField(blank=True, null=True, to='main.avariacarga'),
        ),
    ]