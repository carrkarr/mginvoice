# Generated by Django 3.2.12 on 2022-05-10 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fac', '0007_auto_20220510_0430'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facturas',
            name='FECHA_EMISION',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
