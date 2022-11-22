from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, unique=True, null=True, on_delete=models.CASCADE)
    namaLengkap = models.CharField(max_length=50)

    def __str__(self):
        return self.namaLengkap
    
STATUS_LAKI = (
            ("1", "Jejaka"), 
            ("2", "Duda")
               )
class Suami(models.Model):
    namaSuami = models.CharField(max_length=100)
    nomorKtpSuami = models.CharField(max_length=16)
    tempatLahirSuami = models.CharField(max_length=50)
    tanggalLahirSuami = models.DateField() 
    alamatSuami = models.CharField(max_length=255)
    pekerjaanSuami = models.CharField(max_length=50)
    statusSuami = models.CharField(max_length=1, choices=STATUS_LAKI, default=1)
    fotoSuami = models.ImageField(upload_to='foto/laki', null=True, blank=True)
    
    created = models.DateTimeField(auto_now_add=True, null = True)
    updated = models.DateTimeField(auto_now = True)
    
    def __str__(self):
        return self.namaSuami

STATUS_PEREMPUAN = (
            ("1", "Perawan"), 
            ("2", "Janda")
               )
class Istri(models.Model):
    namaIstri = models.CharField(max_length=100)
    nomorKtpIstri = models.CharField(max_length=16)
    tempatLahirIstri = models.CharField(max_length=50)
    tanggalLahirIstri = models.DateField() 
    alamatIstri = models.CharField(max_length=255)
    pekerjaanIstri = models.CharField(max_length=50)
    statusIstri = models.CharField(max_length=1, choices=STATUS_PEREMPUAN, default=1)
    fotoIstri = models.ImageField(upload_to='foto/perempuan', null=True, blank=True)
    
    created = models.DateTimeField(auto_now_add=True, null = True)
    updated = models.DateTimeField(auto_now = True)
    
    def __str__(self):
        return self.namaIstri
    
class Penghulu(models.Model):
    nama = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nama

def random_penghulu():
    q = Penghulu.objects.order_by('?')[0]
    return q
class Akad(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    
    penghulu = models.ForeignKey(Penghulu, on_delete=models.RESTRICT)
    suami = models.ForeignKey(Suami, on_delete=models.CASCADE)
    istri = models.ForeignKey(Istri, on_delete=models.CASCADE)
    
    waktuAkad = models.DateField()
    jamAkad = models.TimeField()
    mahar = models.CharField(max_length=100)
    lokasi = models.CharField(max_length=100)
    
    diperiksa = models.BooleanField(default= False)
    created = models.DateTimeField(auto_now_add=True, null = True)
    updated = models.DateTimeField(auto_now = True)
    
    def __str__(self):
        return f"Akad {self.suami} dan {self.istri}"
    
    

PIHAK_WALI = (("1", "Suami"), ("2", "Istri"))
HUBUNGAN = (("1", "Bapak"), ("2", "Ibu"), ("3", "Wali"))
class Wali(models.Model):
    akad = models.ForeignKey(Akad, on_delete=models.CASCADE)
    pihak = models.CharField(max_length=1, choices = PIHAK_WALI)
    hubungan = models.CharField(max_length=1, choices=HUBUNGAN)
    nama = models.CharField(max_length=100)
    no_ktp = models.CharField(max_length=16)
    tempatLahir = models.CharField(max_length=50)
    tanggalLahir = models.DateField()
    agama = models.CharField(max_length=20)
    pekerjaan = models.CharField(max_length=50)
    meninggal = models.BooleanField(default=False)   
    
    def __str__(self):
        return f"Perwalian {self.akad}"

