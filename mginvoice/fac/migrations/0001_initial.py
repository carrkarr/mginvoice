# Generated by Django 3.2.12 on 2022-07-30 18:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Afiliado',
            fields=[
                ('ID_AFILIADO', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('NOMBRE_COMPLETO', models.CharField(default='', max_length=240)),
                ('NOMBRE_ALIAS', models.CharField(max_length=80, unique=True)),
                ('COMISION', models.DecimalField(decimal_places=2, default=0.0, max_digits=12)),
                ('APLICA_A', models.CharField(default='', max_length=40)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['NOMBRE_ALIAS'],
            },
        ),
        migrations.CreateModel(
            name='Eemisora',
            fields=[
                ('ID_EMISOR', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('RFC', models.CharField(max_length=20, unique=True)),
                ('NOMBRE', models.CharField(default='', max_length=240)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['NOMBRE'],
            },
        ),
        migrations.CreateModel(
            name='Ereceptora',
            fields=[
                ('ID_RECEPTOR', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('RFC', models.CharField(max_length=20, unique=True)),
                ('NOMBRE', models.CharField(default='', max_length=240)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['NOMBRE'],
            },
        ),
        migrations.CreateModel(
            name='EstadosFac',
            fields=[
                ('ID_ESTADO_FAC', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('NOMBRE', models.CharField(default='', max_length=30)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['NOMBRE'],
            },
        ),
        migrations.CreateModel(
            name='TiposDoc',
            fields=[
                ('ID_TIPO_DOC', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('NOMBRE', models.CharField(default='', max_length=30)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['NOMBRE'],
            },
        ),
        migrations.CreateModel(
            name='Monedas',
            fields=[
                ('ID_MONEDA', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('NOMBRE', models.CharField(default='', max_length=9)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['NOMBRE'],
            },
        ),
        migrations.CreateModel(
            name='Facturas',
            fields=[
                ('ID_FACTURA', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('FOLIO', models.CharField(default='', max_length=30)),
                ('SERIE', models.CharField(default='', max_length=10)),
                ('FECHA_EMISION', models.DateField(blank=True, null=True)),
                ('SUBTOTAL', models.DecimalField(decimal_places=2, default=0.0, max_digits=16)),
                ('TOTAL', models.DecimalField(decimal_places=2, default=0.0, max_digits=19)),
                ('IVA', models.DecimalField(decimal_places=2, default=0.0, max_digits=12)),
                ('TIPO_CAMBIO', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('ID_AFILIADO', models.ForeignKey(default=0, null=True, on_delete=django.db.models.deletion.RESTRICT, to='fac.afiliado')),
                ('ID_EMISOR', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='fac.eemisora')),
                ('ID_ESTADO_FAC', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='fac.estadosfac')),
                ('ID_MONEDA', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='fac.monedas')),
                ('ID_RECEPTOR', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='fac.ereceptora')),
                ('ID_TIPO_DOC', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='fac.tiposdoc')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-FECHA_EMISION'],
            },
        ),
        migrations.AddConstraint(
            model_name='facturas',
            constraint=models.UniqueConstraint(fields=('ID_EMISOR', 'SERIE', 'FOLIO'), name='unique_fac'),
        ),
    ]
