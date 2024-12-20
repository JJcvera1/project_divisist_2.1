# Generated by Django 5.1.2 on 2024-11-11 22:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('divisist', '0002_remove_usuariocarnet_codigo_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='PeriodoAcademico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('periodoAcademico', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='materia',
            name='equivalencia',
            field=models.ManyToManyField(blank=True, to='divisist.materia'),
        ),
        migrations.AlterField(
            model_name='matriculamateria',
            name='periodoAcademico',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='divisist.periodoacademico'),
        ),
    ]
