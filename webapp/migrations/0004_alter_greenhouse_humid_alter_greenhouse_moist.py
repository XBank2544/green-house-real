# Generated by Django 4.2 on 2023-08-12 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_greenhouse_remove_schedule_temp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='greenhouse',
            name='humid',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='greenhouse',
            name='moist',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]