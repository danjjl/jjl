# -*- coding: utf-8 -*-
from django.core.exceptions import ObjectDoesNotExist
from datetime import date
from JJL.Kvoutsot.models import Kvoutsa

#__FUNCTIONS__
#retourne le nom de la kvoutsa actuelle ayant 'age'
def nomKvoutsa(age):
    kvoutsa = ""
    try:
        #kvoutsot born on 01/09/year
        kvoutsa = Kvoutsa.objects.get(date_creation=date(date.today().year + 6 - age, 9, 1))
    except ObjectDoesNotExist:
        #should notify admin
        pass
    return kvoutsa
