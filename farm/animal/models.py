from django.db import models

class Animal(models.Model):

    name = models.CharField(max_length=64)
    species = models.CharField(max_length=64)
    owner = models.ForeignKey('person.Person')

    class Meta:
        app_label = 'animal'
        db_table = 'animal'
        ordering = ('species', 'name')        
