# Generated by Django 5.0.6 on 2024-06-18 10:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agendamentos', '0007_remove_cadastro_cpf_remove_cadastro_telefone_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='disponibilidadec',
            name='foto_sala',
        ),
    ]