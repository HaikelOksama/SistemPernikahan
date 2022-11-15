from django.db import models


# Create your models here.
STATUS_LAKI = (
            ("1", "Jejaka"), 
            ("2", "Duda")
               )
class Suami(models.Model):
    nama = models.CharField(max_length=100)
    nomorKtp = models.CharField(max_length=16, unique=True)
    tanggalLahir = models.DateField() 
    alamat = models.CharField(max_length=255)
    pekerjaan = models.CharField(max_length=50)
    status = models.CharField(max_length=1, choices=STATUS_LAKI, default=1)
    foto = models.ImageField(upload_to='foto/laki', null=True, blank=True)
    
    created = models.DateTimeField(auto_now_add=True, null = True)
    updated = models.DateTimeField(auto_now = True)
    
    def __str__(self):
        return self.nama

STATUS_PEREMPUAN = (
            ("1", "Perawan"), 
            ("2", "Janda")
               )
class Istri(models.Model):
    nama = models.CharField(max_length=100)
    nomorKtp = models.CharField(max_length=16, unique=True)
    tanggalLahir = models.DateField() 
    alamat = models.CharField(max_length=255)
    pekerjaan = models.CharField(max_length=50)
    status = models.CharField(max_length=1, choices=STATUS_PEREMPUAN, default=1)
    foto = models.ImageField(upload_to='foto/perempuan', null=True, blank=True)
    
    created = models.DateTimeField(auto_now_add=True, null = True)
    updated = models.DateTimeField(auto_now = True)
    
    def __str__(self):
        return self.nama
    
class Penghulu(models.Model):
    nama = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nama
    
class Akad(models.Model):
    penghulu = models.ForeignKey(Penghulu, on_delete=models.CASCADE)
    suami = models.ForeignKey(Suami, on_delete=models.CASCADE)
    istri = models.ForeignKey(Istri, on_delete=models.CASCADE)
    
    waktuAkad = models.DateTimeField()
    mahar = models.CharField(max_length=100)
    lokasi = models.CharField(max_length=100)
    
    diperiksa = models.BooleanField(default= False)
    
    def __str__(self):
        return f"Akad {self.suami} dan {self.istri}"

PIHAK_WALI = (("1", "Suami"), ("2", "Istri"))
HUBUNGAN = (("1", "Bapak"), ("2", "Ibu"), ("3", "Wali"))
class Wali(models.Model):
    akad = models.ForeignKey(Akad, on_delete=models.CASCADE)
    pihak = models.CharField(max_length=1, choices = PIHAK_WALI)
    no_ktp = models.CharField(max_length=16, unique = True)
    hubungan = models.CharField(max_length=1, choices=HUBUNGAN)
    nama = models.CharField(max_length=100)
    tempatLahir = models.CharField(max_length=50)
    tanggalLahir = models.DateField()
    agama = models.CharField(max_length=20)
    pekerjaan = models.CharField(max_length=50)
    meninggal = models.BooleanField(default=False)   
    
    def __str__(self):
        return f"Perwalian {self.akad}"
    
    
    