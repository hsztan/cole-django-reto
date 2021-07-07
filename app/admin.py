from django.contrib import admin
from .models import Alumno, Asistencia, Profesor, Nota, Curso
# Register your models here.


@admin.register(Alumno)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre']


@admin.register(Profesor)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'user']


@admin.register(Curso)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre']


@admin.register(Asistencia)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'tipo', 'alumno']


@admin.register(Nota)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'nota', 'fecha', 'alumno']
