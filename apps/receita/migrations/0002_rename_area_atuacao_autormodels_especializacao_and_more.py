# Generated by Django 4.2.5 on 2023-09-27 19:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('receita', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='autormodels',
            old_name='area_atuacao',
            new_name='especializacao',
        ),
        migrations.RemoveField(
            model_name='autormodels',
            name='info_usuario',
        ),
        migrations.AddField(
            model_name='receitamodels',
            name='autor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='receita.autormodels'),
        ),
    ]
