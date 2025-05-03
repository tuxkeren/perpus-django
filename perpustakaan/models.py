from django.db import models

class Kelompok(models.Model):
    nama = models.CharField(max_length=20)
    keterangan = models.TextField(null=True)
    
    def __str__(self):
        return self.nama


class Penerbit(models.Model):
    nama    = models.CharField(max_length=50, null=True)
    alamat  = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.nama


class Buku(models.Model):
    judul = models.CharField(max_length=50)
    penulis = models.CharField(max_length=40)
    penerbit = models.ForeignKey(Penerbit, on_delete=models.CASCADE, null=True)
    jumlah = models.IntegerField(null=True)
    kelompok = models.ForeignKey(Kelompok, on_delete=models.CASCADE, null=True)
    cover = models.ImageField(upload_to='cover/', null=True)
    tanggal = models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
        return self.judul
    


