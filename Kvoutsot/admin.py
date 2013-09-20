from django.contrib import admin
from JJL.Kvoutsot.models import Kvoutsa

class KvoutsaAdmin(admin.ModelAdmin):
    ordering = ('-date_creation',)

admin.site.register(Kvoutsa, KvoutsaAdmin)
