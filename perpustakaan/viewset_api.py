from perpustakaan.models import *
from perpustakaan.serializers import *
from rest_framework import viewsets

class BukuViewset(viewsets.ModelViewSet):
	queryset = Buku.objects.all()
	serializer_class = BukuSerializer
