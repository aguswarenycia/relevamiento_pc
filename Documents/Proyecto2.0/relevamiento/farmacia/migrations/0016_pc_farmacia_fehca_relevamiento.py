# Generated by Django 3.2.3 on 2021-07-02 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farmacia', '0015_auto_20210702_1712'),
    ]

    operations = [
        migrations.AddField(
            model_name='pc_farmacia',
            name='fehca_relevamiento',
            field=models.DateField(blank=True, null=True, verbose_name='Fecha-Relevamiento'),
        ),
    ]