from django.contrib import admin
from perpustakaan.models import *

class BukuAdmin(admin.ModelAdmin):
    list_display = ('judul', 'penulis','penerbit', 'jumlah','kelompok')
    search_fields = ('judul', 'penulis', 'penerbit')
    list_filter = ('kelompok','penerbit')
    list_per_page = 4
    
admin.site.register(Kelompok)
admin.site.register(Penerbit)
admin.site.register(Buku, BukuAdmin)

