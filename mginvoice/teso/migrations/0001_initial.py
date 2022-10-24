# Generated by Django 3.2.12 on 2022-09-26 04:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_userforeignkey.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('fac', '0006_auto_20220926_0415'),
    ]

    operations = [
        migrations.CreateModel(
            name='Repartos',
            fields=[
                ('ID_REPARTO', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('TOTAL_FACTURA', models.DecimalField(decimal_places=2, default=0.0, max_digits=19)),
                ('PORC_RETORNO', models.DecimalField(decimal_places=2, default=0.0, max_digits=12)),
                ('TOTAL_RETORNO', models.DecimalField(decimal_places=2, default=0.0, max_digits=19)),
                ('FECHA_REGISTRO', models.DateField(auto_now_add=True)),
                ('FECHA_IMPRESION', models.DateField(blank=True, null=True)),
                ('FECHA_ENTREGA', models.DateField(blank=True, null=True)),
                ('ID_FACTURA', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='fac.facturas')),
                ('usuario', django_userforeignkey.models.fields.UserForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-FECHA_REGISTRO'],
            },
        ),
        migrations.CreateModel(
            name='FormasPago',
            fields=[
                ('ID_FORMA_PAGO', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('NOMBRE', models.CharField(max_length=30, unique=True)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['NOMBRE'],
            },
        ),
        migrations.AddConstraint(
            model_name='repartos',
            constraint=models.UniqueConstraint(fields=('ID_REPARTO', 'ID_FACTURA'), name='unique_rep'),
        ),
    ]