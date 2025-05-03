from import_export import resources
from perpustakaan.models import *
from import_export.fields import Field


class BukuResource(resources.ModelResource):
	kelompok__nama = Field(attribute='kelompok', column_name='kelompok')
	penerbit__nama = Field(attribute='penerbit', column_name='penerbit')

	class Meta:
		model = Buku
		fields = ['judul','kelompok__nama','penulis','penerbit__nama','jumlah','tanggal']
