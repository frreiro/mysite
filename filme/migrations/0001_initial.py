# Generated by Django 5.1.7 on 2025-03-24 23:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Generos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genero', models.CharField(max_length=100, verbose_name='Genero')),
            ],
        ),
        migrations.CreateModel(
            name='Filmes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filmmax_digitse', models.CharField(max_length=100, verbose_name='Nome')),
                ('quantidade', models.IntegerField(default=0, verbose_name='Quantidade')),
                ('preco', models.FloatField(max_length=2, verbose_name='Preço')),
                ('genero', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='filme.generos')),
            ],
        ),
    ]
