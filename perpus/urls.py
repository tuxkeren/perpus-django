from django.contrib import admin
from django.urls import path

from perpustakaan.views import *
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
   
    # url untuk halaman Admin
    path('admin/', admin.site.urls),


    # untuk halaman Login, Logout, dan Signup
    path('masuk/', LoginView.as_view(), name='masuk'),
    path('keluar/', LogoutView.as_view(next_page='masuk'), name='keluar'),
    path('signup/', signup, name='signup'),


    # url untuk Buku
    path('buku/', buku, name='buku'),
    path('tambah-buku/', tambah_buku, name='tambah_buku'),
    path('buku/ubah/<int:id_buku>', ubah_buku, name='ubah_buku'),
    path('buku/hapus/<int:id_buku>', hapus_buku, name='hapus_buku'),
    

    # url untuk Kelompok
    path('kelompok/', kelompok, name='kelompok'),
    path('tambah-kelompok/', tambah_kelompok, name='tambah_kelompok'),
    path('kelompok/ubah/<int:id_kelompok>', ubah_kelompok, name='ubah_kelompok'),
    path('kelompok/hapus/<int:id_kelompok>', hapus_kelompok, name='hapus_kelompok'),


    # url untuk Penerbit
    path('penerbit/', penerbit, name='penerbit'),
    path('tambah-penerbit/', tambah_penerbit, name='tambah_penerbit'),
    path('penerbit/ubah/<int:id_penerbit>', ubah_penerbit, name='ubah_penerbit'),
    path('penerbit/hapus/<int:id_penerbit>', hapus_penerbit, name='hapus_penerbit'),
    
]


