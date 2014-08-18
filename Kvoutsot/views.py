# -*- coding: utf-8 -*-
from django.core.exceptions import ObjectDoesNotExist
from datetime import date
from JJL.Kvoutsot.models import Kvoutsa

#__FUNCTIONS__
#retourne le nom de la kvoutsa actuelle ayant 'age' en septembre
def nomKvoutsa(age):
    kvoutsa = ""
    try:
        #kvoutsot born on 01/09/year
        if date.today().month < 8:
            age += 1 #kvoutsa is older in january-august
        kvoutsa = Kvoutsa.objects.get(date_creation=date(date.today().year + 6 - age, 9, 1))
    except ObjectDoesNotExist:
        #should notify admin
        pass
    return kvoutsa
