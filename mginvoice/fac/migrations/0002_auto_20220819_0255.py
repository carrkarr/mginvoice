# Generated by Django 3.2.12 on 2022-08-19 02:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fac', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facturas',
            name='ID_ESTADO_FAC',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='fac.estadosfac'),
        ),
        migrations.AlterField(
            model_name='monedas',
            name='NOMBRE',
            field=models.CharField(default='', max_length=9, unique=True),
        ),
    ]