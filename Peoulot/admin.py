from django.contrib import admin
from JJL.Peoulot.models import Peoula

class PeoulaAdmin(admin.ModelAdmin):
    list_display = ('nom', 'age',)
    ordering = ('age', '-date_creation',)
    list_filter = ('age', 'genre', 'theme',)
    search_fields = ('nom',)

admin.site.register(Peoula, PeoulaAdmin)
