from perpustakaan.models import *
from perpustakaan.serializers import *
from rest_framework import viewsets

class BukuViewset(viewsets.ModelViewSet):
	queryset = Buku.objects.all()
	serializer_class = BukuSerializer


class KelompokViewset(viewsets.ModelViewSet):
	queryset = Kelompok.objects.all()
	serializer_class = KelompokSerializer


class PenerbitViewset(viewsets.ModelViewSet):
	queryset = Penerbit.objects.all()
	serializer_class = PenerbitSerializer