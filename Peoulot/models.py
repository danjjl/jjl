# -*- coding: utf-8 -*-
from django.db import models

class Peoula(models.Model):
    CHOIX_AGE = (
        (6, '6-7'),
        (7, '7-8'),
        (8, '8-9'),
        (9, '9-10'),
        (10, '10-11'),
        (11, '11-12'),
        (12, '12-13'),
        (13, '13-14'),
        (14, '14-15'),
        (15, '15-16'),
	(99, 'JJL'),
    )
    nom = models.CharField(max_length=50)
    age = models.IntegerField(choices=CHOIX_AGE)
    theme = models.CharField(max_length=50)
    but = models.CharField(max_length=500)
    genre = models.CharField('Type', max_length=50)
    duree = models.CharField('durée', max_length=30)
    introduction = models.TextField()
    deroulement = models.TextField('déroulement', )
    conclusion = models.TextField()
    materiel = models.TextField('matériel', )
    commentaires = models.TextField(blank=True, )
    variantes = models.TextField(blank=True, )
    date_creation = models.DateField()
    telechargement = models.IntegerField()

    #Delete object instance : delete all attachements
    def delete(self, *args, **kwargs):
        #avoid circular import
        from JJL.Peoulot.views import listePeoulotFiles, deleteFile
        files = listePeoulotFiles(self.pk)
        for filename in files:
            deleteFile(filename)
        super(Peoula, self).delete(*args, **kwargs)

    def __unicode__(self):
        return self.nom

    class Meta:
        ordering = ['age', '-telechargement', '-date_creation']
