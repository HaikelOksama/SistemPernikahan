from django.forms import ModelForm
from django import forms
from .models import Akad, Suami, Istri, Penghulu, Wali, Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm  
from django.core.exceptions import ValidationError  

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['namaLengkap']
   
        widgets = {
            'namaLengkap': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nama Lengkap'}),
        }

class UserForm(UserCreationForm):
    username = forms.CharField(label='' , max_length=150, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))  
   
    password1 = forms.CharField(label='password', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))  
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Konfirmasi Password'}))  
    
    class Meta:
        model = User
        fields = '__all__'
        
class SignUpForm(UserCreationForm):
    username = forms.CharField(label='Username' , max_length=150, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))  
    first_name = forms.CharField(label='Nama' , max_length=150, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nama Anda'})) 
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))  
    password2 = forms.CharField(label='Konfirmasi Password', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Konfirmasi Password'}))  
    class Meta:
        model = User
        fields = ["first_name","username", "password1", "password2"]


class SuamiForm(ModelForm):
    class Meta:
        model = Suami
        fields = '__all__'
        exclude = ['created', 'updated']
        labels = {
            'namaSuami' : 'Nama Calon Suami',
            'nomorKtpSuami': 'Nomor Calon KTP Suami',
            'tanggalLahirSuami': 'Tanggal Lahir Calon Suami',
            'alamatSuami': 'Alamat Calon Suami',
            'pekerjaanSuami': 'Pekerjaan Calon Suami',
            'statusSuami': 'Status Calon Suami',
            'fotoSuami': 'Upload Foto Calon Suami',            
        }
        widgets = {
            'namaSuami': forms.TextInput(attrs={'placeholder': 'Masukkan Nama Calon Suami'}),
            'statusSuami': forms.Select(attrs={
                'class': 'form-control',
            }),
            'nomorKtpSuami': forms.NumberInput(),
            'tanggalLahirSuami': forms.DateInput(attrs={'type': 'date'}, format= '%Y-%m-%d'),
        }

class IstriForm(ModelForm):
    class Meta:
        model = Istri
        fields = '__all__'
        exclude = ['created', 'updated']
        labels = {
            'namaIstri' : 'Nama Calon Istri',
            'nomorKtpIstri': 'Nomor Calon KTP Istri',
            'tanggalLahirIstri': 'Tanggal Lahir Calon Istri',
            'alamatIstri': 'Alamat Calon Istri',
            'pekerjaanIstri': 'Pekerjaan Calon Istri',
            'statusIstri': 'Status Calon Istri',
            'fotoIstri': 'Upload Foto Calon Istri',
        }
        widgets = {
            'namaIstri': forms.TextInput(attrs={'placeholder': 'Masukkan Nama Calon Istri'}),
            'statusIstri': forms.Select(attrs={
                'class': 'form-control',
            }),
            'nomorKtpIstri': forms.NumberInput(),
            'tanggalLahirIstri': forms.DateInput(attrs={'type': 'date'}, format= '%Y-%m-%d'),
        }

class AkadForm(ModelForm): 
    class Meta:
        model = Akad
        fields = '__all__'
        exclude = ['diperiksa', 'suami', 'istri', 'user']
        labels = {
            'mahar' : 'Mahar Pernikahan',
            'lokasi' : 'Tempat Pelaksanaan Akad',
            'waktuAkad': 'Tanggal Pelaksanaan Akad',
            'jamAkad': 'Waktu Pelaksanaan Akad'
        }
        widgets = {
            'penghulu' : forms.Select(attrs={'class':'form-control',}),
            'waktuAkad': forms.DateTimeInput(attrs={'type': 'date'},format= '%Y-%m-%d'),
            'jamAkad': forms.TimeInput(attrs={'type': 'time'},format='%H:%M'),
        }

class AkadEditForm(ModelForm):
    class Meta:
        model = Akad
        fields = '__all__'
        exclude = ['user', 'created', 'updated',]
        labels = {
            'suami' : 'Nama Suami',
            'istri' : 'Nama Istri',
            'waktuAkad' : 'Waktu Akad/Nikah',
            'mahar' : 'Mahar Pernikahan',
            'lokasi' : 'Lokasi Berlangsungnya Akad/Pernikahan',
            'diperiksa' : 'Konfirmasi semua data telah dicek dengan benar'
        }
        widgets = {
            'suami': forms.Select(attrs={'class': 'form-control', 'readonly': 'true', }),
            'istri': forms.Select(attrs={'class': 'form-control', 'readonly': 'true', }),
            
            'penghulu': forms.Select(attrs={'class': 'form-control',}),
            'waktuAkad': forms.DateInput(attrs={'class': 'form-control', 'type': 'date',}, format= '%Y-%m-%d'),
            'jamAkad': forms.TimeInput(attrs={'type': 'time'},format='%H:%M'),
            'mahar': forms.TextInput(attrs={'class': 'form-control', })
        }

class KonfirmasiForm(ModelForm):
    class Meta:
        model = Akad
        fields = ['diperiksa']
        label = {'diperiksa' : 'Konfirmasi semua data telah dicek dengan benar'}
        widgets = {
            'diperiksa': forms.CheckboxInput(attrs={'required': 'true',})
        }

class WaliForm(ModelForm):
    class Meta:
        model = Wali
        fields = '__all__'
        exclude = ['akad', ]
        labels = {
            'nama': 'Nama Wali',
            'no_ktp': 'Nomor KTP',
            'tempatLahir': 'Tempat Lahir Wali',
            'tanggalLahir': 'Tanggal Lahir Wali',
            'meninggal': 'Telah Meninggal Dunia',
        }
        
        widgets = {
            'nama' : forms.TextInput(attrs={'placeholder': 'Masukkan Nama Wali'}),
            'pihak' : forms.Select(attrs={'class': 'form-control'}),
            'hubungan' : forms.Select(attrs={'class': 'form-control'}),
            'no_ktp' : forms.NumberInput(),
            'meninggal': forms.CheckboxInput(attrs={'class': 'form-check-input mt-4 ml-0'}),
            'tanggalLahir': forms.DateInput(attrs={'class': 'form-control', 'type': 'date',} , format= '%Y-%m-%d'),
        }

class PenghuluForm(ModelForm):
    class Meta:
        model = Penghulu
        fields = '__all__'