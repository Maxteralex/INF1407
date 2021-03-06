# Generated by Django 3.1 on 2020-12-02 20:49

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0002_auto_20201202_1116'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='carro',
            options={'permissions': (('gerenciar_carros', 'Pode criar, ver todos, atualizar, remover e ativar/desativar carros'),)},
        ),
        migrations.RenameField(
            model_name='funcionario',
            old_name='hh_semana',
            new_name='horas_semana',
        ),
        migrations.AddField(
            model_name='aluguel',
            name='data_avaliacao',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='aluguel',
            name='status',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='aluguel',
            name='funcionario',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='rental.funcionario'),
        ),
        migrations.AlterField(
            model_name='solicita',
            name='data_solicitacao',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
