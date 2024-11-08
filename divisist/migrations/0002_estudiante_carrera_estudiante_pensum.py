# Generated by Django 5.1.2 on 2024-11-08 02:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('divisist', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='estudiante',
            name='carrera',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='divisist.carrera'),
        ),
        migrations.AddField(
            model_name='estudiante',
            name='pensum',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='divisist.pensum'),
        ),
    ]