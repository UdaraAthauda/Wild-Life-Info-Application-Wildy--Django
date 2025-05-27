from django.contrib import admin
from .models import *

admin.site.register(Region)

class VenomTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'venom_type_translation')

admin.site.register(VenomType, VenomTypeAdmin)

admin.site.register(Snake)