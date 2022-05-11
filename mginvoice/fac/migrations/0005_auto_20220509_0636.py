# Generated by Django 3.2.12 on 2022-05-09 06:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fac', '0004_alter_facturas_index_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facturas',
            name='ID_AFILIADO',
            field=models.ForeignKey(default=0, null=True, on_delete=django.db.models.deletion.RESTRICT, to='fac.afiliado'),
        ),
        migrations.AlterIndexTogether(
            name='facturas',
            index_together=set(),
        ),
        migrations.AddConstraint(
            model_name='facturas',
            constraint=models.UniqueConstraint(fields=('ID_EMISOR', 'SERIE', 'FOLIO', 'TIPO_DOCUMENTO'), name='unique_fac'),
        ),
    ]
