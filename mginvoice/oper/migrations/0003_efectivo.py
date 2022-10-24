# Generated by Django 3.2.12 on 2022-10-23 04:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_userforeignkey.models.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('oper', '0002_alter_depositos_usuario'),
    ]

    operations = [
        migrations.CreateModel(
            name='Efectivo',
            fields=[
                ('ID_EFECTIVO', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('FECHA_DEPOSITO', models.DateField(blank=True, null=True)),
                ('IMPORTE', models.DecimalField(decimal_places=2, default=0.0, max_digits=19)),
                ('PORC_COMI', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('IMPORTE_DISP', models.DecimalField(decimal_places=2, default=0.0, max_digits=19)),
                ('SALDO', models.DecimalField(decimal_places=2, default=0.0, max_digits=19)),
                ('usuario', django_userforeignkey.models.fields.UserForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-FECHA_DEPOSITO'],
            },
        ),
    ]
