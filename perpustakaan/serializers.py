from perpustakaan.models import *
from rest_framework import serializers


class BukuSerializer(serializers.ModelSerializer):
	class Meta:
		model = Buku
		fields = '__all__'


class KelompokSerializer(serializers.ModelSerializer):
	class Meta:
		model = Kelompok
		fields = '__all__'


class PenerbitSerializer(serializers.ModelSerializer):
	class Meta:
		model = Penerbit
		fields = '__all__'