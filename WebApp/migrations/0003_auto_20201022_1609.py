# Generated by Django 3.1.1 on 2020-10-22 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebApp', '0002_auto_20201022_1548'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='vigencia',
            field=models.CharField(choices=[('1 año', '1 año'), ('2 años', '2 años'), ('3 años', '3 años'), ('4 años', '4 años')], max_length=50),
        ),
    ]
