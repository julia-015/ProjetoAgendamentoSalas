# Generated by Django 5.0.6 on 2024-06-18 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agendamentos', '0006_cadastro_reservas_remove_usuario_data_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cadastro',
            name='cpf',
        ),
        migrations.RemoveField(
            model_name='cadastro',
            name='telefone',
        ),
        migrations.AddField(
            model_name='disponibilidadec',
            name='corredor',
            field=models.CharField(default=0, max_length=15),
            preserve_default=False,
        ),
    ]
