# Generated by Django 5.1.2 on 2024-10-29 18:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tiendaRelojesAPP', '0002_remove_filtro_mecanismo_remove_filtro_tipocorrea_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='compra',
            name='Reloj',
        ),
        migrations.RemoveField(
            model_name='reloj',
            name='Filtro',
        ),
        migrations.AlterField(
            model_name='filtro',
            name='precio',
            field=models.CharField(blank=True, choices=[('0-100', '0 a 100€'), ('100-500', '100 a 500€'), ('500-1000', '500 a 1000€'), ('1000-5000', '1000 a 5000€'), ('10000+', 'Más de 10000€')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='filtro',
            name='tipo_correa',
            field=models.CharField(blank=True, choices=[('Acero', 'Acero'), ('Cuero', 'Cuero'), ('Tela', 'Tela')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='filtro',
            name='tipo_visualizacion',
            field=models.CharField(blank=True, choices=[('Digital', 'Digital'), ('Analogico', 'Analógico')], max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='compra',
            name='reloj',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='compras', to='tiendaRelojesAPP.reloj'),
        ),
        migrations.AddField(
            model_name='reloj',
            name='filtro',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='relojes', to='tiendaRelojesAPP.filtro'),
        ),
    ]