# Generated by Django 3.2.3 on 2021-06-10 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farmacia', '0004_programa'),
    ]

    operations = [
        migrations.AddField(
            model_name='provincia',
            name='estado',
            field=models.BooleanField(default=True, verbose_name='estado'),
        ),
    ]
