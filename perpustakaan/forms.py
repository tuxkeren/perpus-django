from django.forms import ModelForm
from django import forms
from perpustakaan.models import *

class FormBuku(ModelForm):
    class Meta:
        model = Buku
        fields = '__all__'
        widgets = {
            'judul'   : forms.TextInput({'class': 'form-control'}),
            'penulis' : forms.TextInput({'class': 'form-control'}),
            'penerbit': forms.Select({'class': 'form-control'}),
            'jumlah'  : forms.NumberInput({'class': 'form-control'}),
            'kelompok': forms.Select({'class': 'form-control'}),
        }

class FormKelompok(ModelForm):
    class Meta:
        model = Kelompok
        fields = '__all__'
        widgets = {
            'nama': forms.TextInput({'class':'form-control'}),
            'keterangan': forms.TextInput({'class':'form-control'}),
        }


class FormPenerbit(ModelForm):
    class Meta:
        model = Penerbit
        fields = '__all__'
        widgets = {
            'nama': forms.TextInput({'class':'form-control'}),
            'alamat': forms.TextInput({'class':'form-control'}),
        }