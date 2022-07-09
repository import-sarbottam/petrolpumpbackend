from django.contrib import admin

# Register your models here.

from .models import Entry, Partyname, Prices

admin.site.register(Entry)
admin.site.register(Partyname)
admin.site.register(Prices)
