# Generated by Django 5.1.2 on 2024-11-09 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tiendaRelojesAPP', '0004_remove_reloj_filtro'),
    ]

    operations = [
        migrations.AddField(
            model_name='reloj',
            name='fotoUrl',
            field=models.CharField(max_length=250, null=True),
        ),
    ]
