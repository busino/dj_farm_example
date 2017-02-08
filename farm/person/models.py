from django.db import models

class Person(models.Model):

    first_name = models.CharField(max_length=64)
    surname = models.CharField(max_length=64)

    class Meta:
        app_label = 'person'
        db_table = 'person'
        ordering = ('surname', 'first_name')       