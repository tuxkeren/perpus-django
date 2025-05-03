from django.shortcuts import redirect, render
from django.contrib import messages

from perpustakaan.models import *
from perpustakaan.forms import *
from django.contrib.auth.decorators import login_required
from django.conf import settings


# ========
# Logic program untuk Buku
# ========

# List all Buku
@login_required(login_url=settings.LOGIN_URL)
def buku(request):
    books = Buku.objects.all() # Mengambil semua data buku dari database
    # books = Buku.objects.filter(kelompok_id__nama='Produktif') # Mengambil data buku tertentu
    konteks = {
        'books': books,
    }
    
    return render(request, 'buku/buku.html', konteks)

# Tambah Buku
@login_required(login_url=settings.LOGIN_URL)
def tambah_buku(request):
    if request.POST:
        form = FormBuku(request.POST)
        if form.is_valid():
            form.save()
            form = FormBuku()
            pesan = 'Data buku berhasil disimpan'
            konteks = {
                'form': form,
                'pesan': pesan,
            }
            
            return render(request, 'buku/buku-tambah.html', konteks)
        
    else:
        form = FormBuku()
        konteks = {
            'form': form,
        }
    
    return render(request, 'buku/buku-tambah.html', konteks)

# Ubah Buku
@login_required(login_url=settings.LOGIN_URL)
def ubah_buku(request, id_buku):
    buku = Buku.objects.get(id=id_buku)
    template = 'buku/buku-ubah.html'
    if request.POST:
        form = FormBuku(request.POST, instance=buku)
        if form.is_valid():
            form.save()
            messages.success(request, 'Data buku berhasil diubah')
            
            return redirect('ubah_buku', id_buku=id_buku)
        
    else:
        form = FormBuku(instance=buku)
        konteks = {
            'form': form,
            'buku': buku,
        }
    
    return render(request, template, konteks)

# Hapus Buku
@login_required(login_url=settings.LOGIN_URL)
def hapus_buku(request, id_buku):
    buku = Buku.objects.filter(id=id_buku)
    buku.delete()
    messages.success(request, 'Data Buku berhasil dihapus')

    return redirect('buku')


# ========
# Logic program untuk Kelompok
# ========

# List all Kelompok
@login_required(login_url=settings.LOGIN_URL)
def kelompok(request):
    groups = Kelompok.objects.all() # Mengambil semua data kelompok dari database
    # groups = Kelompok.objects.filter(nama='Produktif') # Mengambil data kelompok tertentu
    konteks = {
        'groups': groups,
    }
    
    return render(request, 'kelompok/kelompok.html', konteks)


# Tambah Kelompok
@login_required(login_url=settings.LOGIN_URL)
def tambah_kelompok(request):
    if request.POST:
        form = FormKelompok(request.POST)
        if form.is_valid():
            form.save()
            form = FormKelompok()
            pesan = 'Data Kelompok berhasil disimpan'
            konteks = {
                'form': form,
                'pesan': pesan,
            }
            
            return render(request, 'kelompok/kelompok-tambah.html', konteks)
        
    else:
        form = FormKelompok()
        konteks = {
            'form': form,
        }
    
    return render(request, 'kelompok/kelompok-tambah.html', konteks)


# Ubah Kelompok
@login_required(login_url=settings.LOGIN_URL)
def ubah_kelompok(request, id_kelompok):
    groups = Kelompok.objects.get(id=id_kelompok)
    template = 'kelompok/kelompok-ubah.html'
    if request.POST:
        form = FormKelompok(request.POST, instance=kelompok)
        if form.is_valid():
            form.save()
            messages.success(request, 'Data kelompok berhasil diubah')
            
            return redirect('ubah_kelompok', id_kelompok=id_kelompok)
        
    else:
        form = FormKelompok(instance=kelompok)
        konteks = {
            'form': form,
            'kelompok': kelompok,
        }
    
    return render(request, template, konteks)


# Hapus Kelompok
@login_required(login_url=settings.LOGIN_URL)
def hapus_kelompok(request, id_kelompok):
    kelompok = Kelompok.objects.filter(id=id_kelompok)
    kelompok.delete()
    messages.success(request, 'Data Kelompok berhasil dihapus')

    return redirect('kelompok')


# ========
# Logic program untuk Penerbit
# ========

# List all Penerbit
@login_required(login_url=settings.LOGIN_URL)
def penerbit(request):
    publishers = Penerbit.objects.all() # Mengambil semua data penerbit dari database
    # Publishers = Penerbit.objects.filter(nama='Produktif') # Mengambil data Penerbit tertentu
    konteks = {
        'publishers': publishers,
    }
    
    return render(request, 'penerbit/penerbit.html', konteks)


# Tambah Penerbit
@login_required(login_url=settings.LOGIN_URL)
def tambah_penerbit(request):
    if request.POST:
        form = FormPenerbit(request.POST)
        if form.is_valid():
            form.save()
            form = FormPenerbit()
            pesan = 'Data Kelompok berhasil disimpan'
            konteks = {
                'form': form,
                'pesan': pesan,
            }
            
            return render(request, 'penerbit/penerbit-tambah.html', konteks)
        
    else:
        form = FormPenerbit()
        konteks = {
            'form': form,
        }
    
    return render(request, 'penerbit/penerbit-tambah.html', konteks)


# Ubah Penerbit
@login_required(login_url=settings.LOGIN_URL)
def ubah_penerbit(request, id_penerbit):
    publishers = Penerbit.objects.get(id=id_penerbit)
    template = 'penerbit/penerbit-ubah.html'
    if request.POST:
        form = FormPenerbit(request.POST, instance=penerbit)
        if form.is_valid():
            form.save()
            messages.success(request, 'Data penerbit berhasil diubah')
            
            return redirect('ubah_penerbit', id_penerbit=id_penerbit)
        
    else:
        form = FormPenerbit(instance=penerbit)
        konteks = {
            'form': form,
            'penerbit': penerbit,
        }
    
    return render(request, template, konteks)


# Hapus Penerbit
@login_required(login_url=settings.LOGIN_URL)
def hapus_penerbit(request, id_penerbit):
    penerbit = Penerbit.objects.get(id=id_penerbit)
    penerbit.delete()
    messages.success(request, 'Data Penerbit berhasil dihapus')

    return redirect('penerbit')
