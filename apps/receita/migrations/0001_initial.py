# Generated by Django 4.2.5 on 2023-09-27 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AutorModels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=40)),
                ('cpf', models.CharField(max_length=11)),
                ('area_atuacao', models.CharField(max_length=40)),
                ('info_usuario', models.TextField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='ReceitaModels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo_receita', models.CharField(max_length=40)),
                ('descricao_receita', models.TextField(max_length=2000)),
            ],
        ),
    ]
