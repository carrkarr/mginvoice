# Generated by Django 3.2.12 on 2022-05-10 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fac', '0006_alter_facturas_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='facturas',
            options={'ordering': ['-FECHA_EMISION']},
        ),
        migrations.RemoveConstraint(
            model_name='facturas',
            name='unique_fac',
        ),
        migrations.AddConstraint(
            model_name='facturas',
            constraint=models.UniqueConstraint(fields=('ID_EMISOR', 'SERIE', 'FOLIO', 'ESTADO_FACTURA'), name='unique_fac'),
        ),
    ]
