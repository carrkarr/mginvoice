# Generated by Django 3.2.12 on 2022-05-07 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fac', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='afiliado',
            name='NOMBRE_ALIAS',
            field=models.CharField(max_length=80, unique=True),
        ),
        migrations.AlterField(
            model_name='eemisora',
            name='RFC',
            field=models.CharField(max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='ereceptora',
            name='RFC',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
