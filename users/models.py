from django.db import models

class User(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=150, blank=False, default='')
    dob = models.DateField(blank=False, null=True)

    class meta:
        ordering = ('name',)
