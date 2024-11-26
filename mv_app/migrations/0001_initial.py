# Generated by Django 5.1.3 on 2024-11-26 04:05

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Estilista',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre completo')),
                ('especialidad', models.CharField(max_length=100, verbose_name='Especialidad')),
                ('experiencia', models.PositiveIntegerField(verbose_name='Años de experiencia')),
                ('disponibilidad', models.BooleanField(default=True, verbose_name='Disponible')),
                ('telefono', models.CharField(blank=True, max_length=15, null=True, verbose_name='Teléfono de contacto')),
                ('correo', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Correo electrónico')),
                ('foto', models.ImageField(blank=True, null=True, upload_to='estilistas/', verbose_name='Foto')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
            ],
        ),
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre del Servicio')),
                ('categoria', models.CharField(choices=[('uñas', 'Uñas'), ('pelo', 'Pelo'), ('depilacion', 'Depilación'), ('pestañas', 'Pestañas')], max_length=20, verbose_name='Categoría')),
                ('descripcion', models.TextField(verbose_name='Descripción')),
                ('duracion', models.PositiveIntegerField(verbose_name='Duración (minutos)')),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Precio')),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('telefono', models.CharField(blank=True, max_length=15, null=True)),
                ('direccion', models.CharField(blank=True, max_length=100, null=True)),
                ('fecha_registro', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Cita',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_cita', models.DateTimeField()),
                ('hora_cita', models.TimeField()),
                ('estado_cita', models.CharField(choices=[('Pendiente', 'Pendiente'), ('Confirmada', 'Confirmada'), ('Cancelada', 'Cancelada')], default='Pendiente', max_length=10)),
                ('comentarios', models.TextField(blank=True, null=True)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='citas_cliente', to='mv_app.cliente')),
                ('estilista', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='citas_estilista', to='mv_app.estilista')),
            ],
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('hora', models.TimeField()),
                ('estilista', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mv_app.estilista')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
