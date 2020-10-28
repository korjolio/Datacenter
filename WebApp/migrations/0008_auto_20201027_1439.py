# Generated by Django 3.1.1 on 2020-10-27 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebApp', '0007_remove_contacto_f_cumple'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacto',
            name='tipo_consulta',
            field=models.IntegerField(choices=[(0, 'Consulta'), (1, 'Reclamo'), (2, 'Sugerencia'), (3, 'Felicitaciones')], verbose_name='Tipo de consulta'),
        ),
    ]