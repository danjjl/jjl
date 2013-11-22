# -*- coding: utf-8 -*-
from django.http import Http404
from django.views.generic import ListView, DetailView, DeleteView
from django.views.generic.edit import CreateView, UpdateView
from django.core.exceptions import ObjectDoesNotExist
from django.template import RequestContext
from django.template.defaultfilters import slugify
from django.conf import settings
from django.contrib import messages

from django.forms.formsets import formset_factory
from django.shortcuts import render_to_response, redirect, get_object_or_404

from datetime import *
import glob
import os
from os import remove, path

from JJL.Peoulot.models import Peoula
from JJL.Kvoutsot.models import Kvoutsa
from JJL.Peoulot.forms import PeoulaForm, UploadFileForm

#__LIST DES PÉOULOT__
class ListPeoulot(ListView):
    model = Peoula #List péoulot
    context_object_name = 'peoulot'

    #determine week or all
    def get_queryset(self):
        self.toutes = 'toutes' in self.kwargs
        return Peoula.objects.all()

    #extra context
    def get_context_data(self, **kwargs):
        context = super(ListPeoulot, self).get_context_data(**kwargs)
        #Toutes
        if self.toutes:
            context['pageTitle'] = 'Toutes les péoulot'
            context['trier'] = True
        #Péoulot de la semaine
        else:
            context['pageTitle'] = 'Péoulot de la semaine'
            context['peoulot'] = context['peoulot'].filter(date_creation__gte=(date.today() - timedelta(10)))
            context['trier'] = False
        return context


#__DÉTAIL PÉOULA__
class LirePeoula(DetailView):
    model = Peoula #List péoulot
    context_object_name = 'peoula'
    template_name = 'Peoulot/peoula_detail.html'

    #extra context
    def get_context_data(self, **kwargs):
        context = super(LirePeoula, self).get_context_data(**kwargs)
        context['pageTitle'] = u'Péoula - ' + self.object.nom
        context['pieceJointe'] = listePeoulotFiles(self.object.id)
        try:
            context['kvoutsa'] = Kvoutsa.objects.get(date_creation=date(date.today().year + 6 - self.object.age, 9, 1)) #TODO moche récupère la kvoutsa
        except ObjectDoesNotExist:
           print 'Did not find a kvoutsa for that age'
        return context

    #On view add download
    def get_object(self):
        object = super(LirePeoula, self).get_object()
        object.telechargement += 1
        object.save()
        return object

#__AJOUTER & MODIFIER__
def ajouterModifier(request, pk=0):
    #Edit
    if pk != 0:
        #Retrieve Peoula
        peoula = get_object_or_404(Peoula, id=pk)
        url = 'modifier/' + str(pk)
        title = u'Modifier la péoula ' + peoula.nom
        files = listePeoulotFiles(peoula.id)
        bouton = 'Modifier'
    #New
    else:
        url = 'ajouter/'
        title = 'Ajouter une Péoula'
        files = ''
        bouton = 'Ajouter'

    peoulaFormSet = PeoulaForm
    fileFormSet = UploadFileForm

    #Submiting
    if request.method == 'POST':
            if pk != 0:
                peoula_FormSet = peoulaFormSet(request.POST, prefix='peoula', instance=peoula)
            else:
                peoula_FormSet = peoulaFormSet(request.POST, prefix='peoula')
            file_FormSet = fileFormSet(request.POST, request.FILES, prefix='file')
            #Delete attachement submit
            if 'delete' in request.POST:
                deleteFile(request.POST['delete'])
                files = listePeoulotFiles(peoula.id)
                messages.info(request, u'La pièce jointe ' + request.POST['delete'] + u' a été suprimée de manière irrévocable.')
            else:
                if peoula_FormSet.is_valid() and file_FormSet.is_valid():
                    #Save Peoula
                    if pk == 0:
                        peoula_FormSet.instance.date_creation = date.today()
                        peoula_FormSet.instance.telechargement = 0
                        messages.success(request, u'La péoula ' + peoula_FormSet.instance.nom + u' a été ajoutée à la, tjs grandissante, liste des péoulot.')
                    else:
                        messages.info(request, u'La péoula ' + peoula_FormSet.instance.nom + u' a été modifiée.')
                    peoula = peoula_FormSet.save()
                    #Save file
                    for files in request.FILES.getlist('file-file'):
                        handle_uploaded_file(files, peoula.id)
                    return redirect('liste')

    #Display form
    else:
        #Edit
        if pk != 0:
            peoula_FormSet = peoulaFormSet(instance=peoula, prefix='peoula')
        #New
        else:
            peoula_FormSet = peoulaFormSet(prefix='peoula')
        file_FormSet = fileFormSet(prefix='file')

    return render_to_response('Peoulot/peoula_form.html', {
        'pageTitle' : title,
        'peoulaForm': peoula_FormSet,
        'fileForm': file_FormSet,
        'url' : url,
        'files' : files,
        'bouton' : bouton,
    }, context_instance=RequestContext(request))

#__SUPPRIMER PÉOULA__
def supprimerPeoula(request, pk):
    peoula = get_object_or_404(Peoula, id=pk)
    messages.info(request, u'La péoula ' + peoula.nom + u' a été suprimée de manière irrévocable.')
    peoula.delete()
    return redirect('liste')

#__FUNCTIONS__
#Slugify filename
def fileify(filename):
    filename = os.path.splitext(filename)
    return slugify(filename[0]) + filename[1]

def handle_uploaded_file(upFile, pk):
    with open(settings.MEDIA_ROOT[0] + '/Peoulot/' + str(pk) + '-' + fileify(upFile.name), 'wb+') as destination:
        for chunk in upFile.chunks():
            destination.write(chunk)

def listePeoulotFiles(pk):
    files = glob.glob(settings.MEDIA_ROOT[0] + '/Peoulot/'+ str(pk) +'-*')
    for i in range(0, len(files)):
        files[i] = files[i][len(settings.MEDIA_ROOT[0] + '/Peoulot/'):]
    return files

def deleteFile(filename):
    if os.path.isfile(settings.MEDIA_ROOT[0] + '/Peoulot/' + filename):
        os.remove(settings.MEDIA_ROOT[0] + '/Peoulot/' + filename)
    else:
        raise Http404
