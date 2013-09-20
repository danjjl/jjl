from django.db import models

class Kvoutsa(models.Model):
    nom = models.CharField(max_length=30, blank=False)
    date_creation = models.DateField()

    def __unicode__(self):
        return self.nom
