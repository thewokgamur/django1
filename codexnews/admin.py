from django.contrib import admin
from core.models import berita,kategori
# Register your models here.

class categoriesAdmin(admin.ModelAdmin):
    list_display = ['namakategori']
    search_fields = ['namakategori']

admin.site.register(kategori,categoriesAdmin)

class beritaAdmin(admin.ModelAdmin):
    list_display = ['judul', 'isi', 'kategori','kategoriid','gambar','penulis','deskripsi','status']
    search_fields = ['judul','kategori_name']
    autocomplete_fields = ['kategori']

admin.site.register(berita,beritaAdmin)