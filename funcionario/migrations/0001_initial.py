# Generated by Django 4.2.3 on 2024-12-01 20:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0002_usuario_delete_userprofileexample'),
    ]

    operations = [
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('usuario_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='users.usuario')),
                ('cargo', models.CharField(max_length=50)),
                ('salario', models.DecimalField(decimal_places=2, max_digits=10)),
                ('data_admissao', models.DateField()),
                ('horario_trabalho_inicio', models.TimeField()),
                ('horario_trabalho_fim', models.TimeField()),
            ],
            options={
                'verbose_name': 'Funcionário',
                'verbose_name_plural': 'Funcionários',
            },
            bases=('users.usuario',),
        ),
    ]
