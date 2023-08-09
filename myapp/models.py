from django.db import models

class Project(models.Model):
    '''
    Modelo que representa un proyecto
    '''

    name = models.CharField(max_length=50, help_text='ingrese el nombre del proyecto')

class Task(models.Model):
    '''
    Modelo que representa una tarea de un proyecto
    '''
    title = models.CharField(max_length=200, help_text='ingrese el titulo de la tarea')
    description = models.TextField(help_text='ingrese la descripción de la tarea')
    project = models.ForeignKey(Project, on_delete=models.CASCADE)