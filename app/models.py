from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.


class Alumno(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255, blank=False, null=False)
    status = models.IntegerField(default=1)

    class Meta:
        db_table = 'alumno'
        verbose_name = 'Alumno'
        verbose_name_plural = 'Alumnos'
        ordering = ['id']

    def __str__(self):
        return self.nombre


class Profesor(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    dni = models.IntegerField(blank=False, null=False)
    status = models.IntegerField(default=1)

    class Meta:
        db_table = 'profesor'
        verbose_name = 'Profesor'
        verbose_name_plural = 'Profesores'
        ordering = ['id']

    def __str__(self):
        return self.user.username


class Curso(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255, blank=False, null=False)
    status = models.IntegerField(default=1)

    class Meta:
        db_table = 'curso'
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'
        ordering = ['id']

    def __str__(self):
        return self.nombre


class Asistencia(models.Model):
    id = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=255, blank=False, null=False)
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    fecha = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'asistencia'
        verbose_name = 'Asistencia'
        verbose_name_plural = 'Asistencias'
        ordering = ['id']

    def __str__(self):
        return self.tipo


class Nota(models.Model):
    id = models.AutoField(primary_key=True)
    nota = models.IntegerField(validators=[
        MaxValueValidator(20),
        MinValueValidator(0)
    ], blank=False, null=False)
    fecha = models.DateField()
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)

    class Meta:
        db_table = 'notas'
        verbose_name = 'Nota'
        verbose_name_plural = 'Notas'
        ordering = ['id']

    def __str__(self):
        return self.alumno
