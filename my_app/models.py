from django.db import models

# Create your models here.
class Project(models.Model):
    """
    Project: This class represents a table called project in the database.
    It stores basic information about a project.
    
    Attributes.
    
    name (CharField): Field that stores the name of a project in the Project
    table.
    """
    name = models.CharField(max_length=200)
    
class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    # defines relationship, deletes related data
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
