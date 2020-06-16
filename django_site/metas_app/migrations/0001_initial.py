# Generated by Django 3.0.3 on 2020-06-04 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Meta1P',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=256)),
                ('cod_departamento', models.PositiveIntegerField()),
                ('cod_subdepartamento', models.IntegerField()),
                ('cod_segmento', models.PositiveIntegerField()),
                ('cod_marca_propria', models.IntegerField()),
                ('alcance_tv_shop', models.CharField(blank=True, max_length=1, null=True)),
                ('cod_dispositivo_origem', models.PositiveIntegerField()),
                ('cod_unidade_negocio', models.PositiveIntegerField()),
                ('dia', models.DateField()),
                ('valor_calculado', models.DecimalField(decimal_places=2, max_digits=30)),
                ('valor_calc_alcance_shop', models.DecimalField(blank=True, decimal_places=2, max_digits=30, null=True)),
                ('percentual_margem_orcada', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
    ]