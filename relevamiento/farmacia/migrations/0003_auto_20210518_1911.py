# Generated by Django 3.2.2 on 2021-05-18 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farmacia', '0002_auto_20210518_1818'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pc_farmacia',
            name='RAM_disponible',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='ram_disponible'),
        ),
        migrations.AlterField(
            model_name='pc_farmacia',
            name='RAM_tot',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='ram_total'),
        ),
        migrations.AlterField(
            model_name='pc_farmacia',
            name='RAM_usada',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='ram_usada'),
        ),
        migrations.AlterField(
            model_name='pc_farmacia',
            name='arquitectura_so',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='arquitectura_so'),
        ),
        migrations.AlterField(
            model_name='pc_farmacia',
            name='cores_fisicos',
            field=models.IntegerField(blank=True, null=True, verbose_name='cores_fisicos'),
        ),
        migrations.AlterField(
            model_name='pc_farmacia',
            name='cores_totales',
            field=models.IntegerField(blank=True, null=True, verbose_name='cores_totales'),
        ),
        migrations.AlterField(
            model_name='pc_farmacia',
            name='ip_publica',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='ip_publica'),
        ),
        migrations.AlterField(
            model_name='pc_farmacia',
            name='nombre_pc',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='nombre_pc'),
        ),
        migrations.AlterField(
            model_name='pc_farmacia',
            name='procesador',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='procesador'),
        ),
        migrations.AlterField(
            model_name='pc_farmacia',
            name='tipo_maquina',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='tipo_maquina'),
        ),
    ]
