# Generated by Django 5.1.2 on 2024-11-11 14:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('director', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreCompleto', models.CharField(max_length=100)),
                ('fechaNacimiento', models.DateField()),
                ('codigo', models.CharField(max_length=15)),
                ('documento', models.CharField(max_length=20)),
                ('celular', models.CharField(max_length=10)),
                ('correoPersonal', models.CharField(max_length=100, unique=True)),
                ('correoInstitucional', models.CharField(max_length=100, unique=True)),
                ('direccion', models.CharField(max_length=100)),
                ('grupoSanguineo', models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Facultad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Horario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dia', models.CharField(max_length=10)),
                ('horaInicio', models.CharField(max_length=7)),
                ('horaFin', models.CharField(max_length=7)),
            ],
        ),
        migrations.CreateModel(
            name='Carrera',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('departamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='divisist.departamento')),
            ],
        ),
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('persona_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='divisist.persona')),
                ('estadoAcademico', models.CharField(max_length=20)),
                ('numeroMatricula', models.CharField(max_length=20)),
                ('fechaInscripcion', models.DateField()),
            ],
            bases=('divisist.persona',),
        ),
        migrations.CreateModel(
            name='AppUser',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=50, unique=True)),
                ('username', models.CharField(max_length=50)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_superuser', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
                ('persona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='persona_user', to='divisist.persona')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='departamento',
            name='facultad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='divisist.facultad'),
        ),
        migrations.CreateModel(
            name='Materia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('codigo', models.CharField(max_length=20)),
                ('creditos', models.IntegerField()),
                ('hasEquivalency', models.BooleanField(default=False)),
                ('cupos', models.IntegerField()),
                ('equivalencia', models.ManyToManyField(to='divisist.materia')),
                ('horario', models.ManyToManyField(to='divisist.horario')),
            ],
        ),
        migrations.CreateModel(
            name='Pensum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('carrera', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='carreras_de_pensum', to='divisist.carrera')),
            ],
        ),
        migrations.AddField(
            model_name='carrera',
            name='pensum',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='pensums_de_carrera', to='divisist.pensum'),
        ),
        migrations.CreateModel(
            name='Semestre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('materias', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='semestres', to='divisist.materia')),
            ],
        ),
        migrations.AddField(
            model_name='pensum',
            name='semestres',
            field=models.ManyToManyField(to='divisist.semestre'),
        ),
        migrations.AddField(
            model_name='materia',
            name='semestre',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='divisist.semestre'),
        ),
        migrations.CreateModel(
            name='UsuarioCarnet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreCompleto', models.CharField(max_length=100)),
                ('codigo', models.CharField(max_length=15)),
                ('documento', models.CharField(max_length=20)),
                ('grupoSanguineo', models.CharField(max_length=3)),
                ('nombreCarrera', models.CharField(max_length=100)),
                ('carrera', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='divisist.carrera')),
                ('persona', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='usuario_carnet_persona', to='divisist.persona')),
            ],
        ),
        migrations.CreateModel(
            name='NotaMateria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('periodoAcademico', models.CharField(max_length=100)),
                ('primerPrevio', models.FloatField()),
                ('segundoPrevio', models.FloatField()),
                ('tercerPrevio', models.FloatField()),
                ('examenFinal', models.FloatField()),
                ('materia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='divisist.materia')),
                ('estudiante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='divisist.estudiante')),
            ],
        ),
        migrations.CreateModel(
            name='MatriculaMateria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('periodoAcademico', models.CharField(max_length=100)),
                ('materia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='divisist.materia')),
                ('estudiante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='divisist.estudiante')),
            ],
        ),
        migrations.CreateModel(
            name='HistoricoNotas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('periodoAcademico', models.CharField(max_length=100)),
                ('materias', models.ManyToManyField(to='divisist.materia')),
                ('estudiante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='divisist.estudiante')),
            ],
        ),
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
        migrations.CreateModel(
            name='Asistencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('horario', models.DateField()),
                ('materia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='divisist.materia')),
                ('estudiantes', models.ManyToManyField(to='divisist.estudiante')),
            ],
        ),
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('persona_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='divisist.persona')),
                ('tipoVinculacion', models.CharField(max_length=20)),
                ('especialidad', models.CharField(max_length=50)),
                ('departamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='divisist.departamento')),
            ],
            bases=('divisist.persona',),
        ),
        migrations.AddField(
            model_name='materia',
            name='profesor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='divisist.profesor'),
        ),
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mensajes', models.CharField(max_length=100)),
                ('materia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='divisist.materia')),
                ('participantes', models.ManyToManyField(to='divisist.estudiante')),
                ('moderador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='divisist.profesor')),
            ],
        ),
    ]
