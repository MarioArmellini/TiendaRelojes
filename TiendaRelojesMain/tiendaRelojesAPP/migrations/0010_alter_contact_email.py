# Generated by Django 5.1.2 on 2024-12-11 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tiendaRelojesAPP', '0009_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]