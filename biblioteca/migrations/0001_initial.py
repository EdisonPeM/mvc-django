# Generated by Django 4.2.13 on 2024-05-21 03:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('codigo_autor', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('nombre_autor', models.CharField(max_length=50)),
                ('nacionalidad', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'autores',
            },
        ),
        migrations.CreateModel(
            name='Editorial',
            fields=[
                ('codigo_editorial', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('nombre_editorial', models.CharField(max_length=30)),
                ('contacto', models.CharField(max_length=30)),
                ('telefono', models.CharField(max_length=9)),
            ],
            options={
                'db_table': 'editoriales',
            },
        ),
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('id_genero', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre_genero', models.CharField(max_length=40)),
                ('descripcion', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'generos',
            },
        ),
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('codigo_libro', models.CharField(max_length=9, primary_key=True, serialize=False)),
                ('nombre_libro', models.CharField(max_length=50)),
                ('existencias', models.IntegerField()),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('descripcion', models.TextField()),
                ('codigo_autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='biblioteca.autor')),
                ('codigo_editorial', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='biblioteca.editorial')),
                ('id_genero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='biblioteca.genero')),
            ],
            options={
                'db_table': 'libros',
            },
        ),
    ]
