from import_export import resources
from perpustakaan.models import *

class BukuResource(resources.ModelResource):
	class Meta:
		model = Buku
		fields = ['judul','kelompok__nama','penulis','penerbit__nama','jumlah','tanggal']
