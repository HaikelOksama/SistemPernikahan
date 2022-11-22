from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from datetime import date

from .models import Suami, Istri, Penghulu, Akad, Wali
from .forms import AkadForm, PenghuluForm, SignUpForm, SuamiForm, IstriForm, AkadEditForm, WaliForm, KonfirmasiForm, ProfileForm, UserForm

def landing(request):
    return render(request, 'base/start.html', {})

def register(request):
    userForm = SignUpForm()
    if request.method == 'POST':
        userForm = SignUpForm(request.POST)
        if userForm.is_valid():
            print(request.POST)
            newUser = userForm.save()
            print(newUser)
            messages.success(request, 'daftarSukses')
            return redirect('landing')

            
    context = {
        'userForm': userForm,
    }
    return render(request, 'base/register.html', context)

def login_view(request):
    if request.user.is_authenticated:
        return redirect('landing')
    if request.method == 'POST':
        print(request.POST)
        usernameIn = request.POST['username']
        passwordIn = request.POST['password']
        
        user = authenticate(request, username = usernameIn, password=passwordIn)
        if user is not None:
            auth = User.objects.get(username=usernameIn)
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Username or Password anda Salah!')

    return render(request, 'base/login.html')

def index(request):
    page = 'Dashboard'
    akad = Akad.objects.all()
    pending = Akad.objects.filter(diperiksa = False)
    penghulu = Penghulu.objects.all()
    akadUser = Akad.objects.filter(user = request.user)
    context = {
        'page': page,
        'akad': akad,
        'akadUser': akadUser,
        'penghulu': penghulu,
        'pending': pending,
    }
    return render(request, 'base/index.html', context)

def akad_view(request):
    page = 'Akad'
    akadModels = Akad.objects.all()
    for wali in akadModels:
        print(wali.wali_set.all())
    context = {
        'akadList' : akadModels,
        'page' : page,
    }
    return render(request, 'base/akad.html', context)

def daftar_akad_view(request):
    page = 'Pendaftaran Pernikahan Baru'
    formAkad = AkadForm()
    formIstri = IstriForm()
    formSuami = SuamiForm()
    
    if request.method == 'POST':
        formIstri = IstriForm(request.POST, request.FILES)
        formSuami = SuamiForm(request.POST, request.FILES)
        formAkad = AkadForm(request.POST)
        if formIstri.is_valid() and formSuami.is_valid() and formAkad.is_valid():
            istri = formIstri.save()
            suami = formSuami.save()
            akad = formAkad.save(commit=False)
            akad.user = request.user
            akad.suami = suami
            akad.istri = istri
            akad.save()
            messages.success(request, f'{akad} Berhasil Titambahkan')
            return redirect('akad')
    
    
    context = {
        'page': page,
        'formAkad': formAkad,
        'formIstri': formIstri,
        'formSuami': formSuami
    } 
    
    return render(request, 'base/daftar_akad.html', context)

def data_suami_view(request):
    page = 'Data Suami'
    suamiList = Suami.objects.all()
    
    context = {
        'page': page,
        'suamiList': suamiList,
    }
    
    return render(request, 'base/data_suami_istri.html', context)

def data_istri_view(request):
    page = 'Data Istri'
    suamiList = Istri.objects.all()
    
    context = {
        'page': page,
        'istriList': suamiList,
    }
    
    return render(request, 'base/data_suami_istri.html', context)

def detail_akad_view(request, pk):
    akad = Akad.objects.get(id=pk)
    page = f'Detail Pernikahan {akad}'
    form = AkadEditForm(instance = akad)
    confirm = KonfirmasiForm(instance = akad, use_required_attribute=True)
    listWali = akad.wali_set.all()
    # print(listWali)
   
    if request.method == 'POST':  
        if request.POST.get('diperiksa'):
            confirm = KonfirmasiForm(request.POST, instance = akad)
            if confirm != None:
                if confirm.is_valid():
                    confirm.save()
                    messages.success(request, f'{akad} Telah Disetujui')
                    return redirect('akad')
        else:           
            form =  AkadEditForm(request.POST, instance = akad)
            if form.is_valid():
                newAkad = form.save(commit=False)
                newAkad.suami = akad.suami
                newAkad.istri = akad.istri
                newAkad.save()
                messages.success(request, f'{akad} Berhasil Dirubah')
                return redirect('akad')
        
    context = {
        'page': page,
        'akad': akad,
        'form': form,
        'listWali': listWali
    }
    return render(request, 'base/detail_akad.html', context)

def hapus_akad(request, pk):
    akad = Akad.objects.get(id=pk)
    akad.suami.delete()
    akad.istri.delete()
    messages.warning(request, f'Data {akad} Telah Dihapus')
    akad.delete()
    return redirect('akad')

def tambah_wali(request, pk):
    akad = Akad.objects.get(id=pk)
    page = f'Tambah Wali {akad}'
    form = WaliForm
    if request.method == 'POST':
        form = WaliForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.akad = akad
            instance.save()
            messages.success(request, 'Wali Berhasil Ditambahkan')
            return redirect('detail_akad', pk)
    
    context = {
        'page': page,
        'akad': akad,
        'form': form
    }
    return render(request, 'base/tambah_wali.html', context)

def ubah_wali(request, akad, pk):
    akad = Akad.objects.get(id=akad)
    wali = Wali.objects.get(id=pk)
    page = f'Ubah Data Wali'
    form = WaliForm(instance = wali)
    if request.method == 'POST':
        form = WaliForm(request.POST, instance=wali)
        if form.is_valid():
            form.save()
            messages.success(request, f'Wali {wali.nama} Berhasil Diubah')
            return redirect('detail_akad', akad.id)
    
    context = {
        'wali': wali,
        'page': page,
        'akad': akad,
        'form': form
    }
    return render(request, 'base/tambah_wali.html', context)

def hapus_wali(request,akad, pk):
    wali = Wali.objects.get(id=pk)
    wali.delete(keep_parents=True)
    messages.warning(request, f'Data Wali {wali.nama} Telah Dihapus')
    return redirect('detail_akad', akad)

def edit_suami_view(request, pk):
    suami = Suami.objects.get(id=pk)
    page = f'Ubah Data Suami'
    form = SuamiForm(instance=suami)
    
    if request.method == 'POST':
        form = SuamiForm(request.POST,request.FILES, instance=suami)
        if form.is_valid():
            form.save()
            messages.success(request, f'Data Suami {suami} Berhasil Dirubah')
            return redirect('data-suami')

    context = {
        'page': page,
        'suami': suami,
        'form': form
    }
    return render(request, 'base/edit_pasangan.html', context)

def edit_istri_view(request, pk):
    istri = Istri.objects.get(id=pk)
    page = f'Ubah Data Istri'
    form = IstriForm(instance=istri)
    
    if request.method == 'POST':
        form = IstriForm(request.POST,request.FILES, instance=istri)
        if form.is_valid():
            form.save()
            messages.success(request, f'Data Istri {istri} Berhasil Dirubah')
            return redirect('data-istri')

    context = {
        'page': page,
        'istri': istri,
        'form': form
    }
    return render(request, 'base/edit_pasangan.html', context)


def penghulu_view(request):
    penghulu = Penghulu.objects.all()
    page = 'Data Penghulu'
    
    context = {
        'penghulu': penghulu,
        'page': page
    }
    return render(request, 'base/penghulu.html', context)

def tambah_penghulu(request):
    page = 'Tambah Penghulu'
    form = PenghuluForm()
    if request.method == 'POST':
        form = PenghuluForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Penghulu Berhasil Ditambahkan')
            return redirect('penghulu')
    context = {
        'page': page,
        'form': form
    }
    return render(request, 'base/tambah_penghulu.html', context)

def ubah_penghulu(request, pk):
    page = 'Ubah Data Penghulu'
    penghulu = Penghulu.objects.get(id=pk)
    form = PenghuluForm(instance=penghulu)
    if request.method == 'POST':
        form = PenghuluForm(request.POST, instance=penghulu)
        if form.is_valid():
            form.save()
            messages.success(request, 'Penghulu Berhasil Dirubah')
            return redirect('penghulu')
    context = {
        'penghulu': penghulu,
        'page': page,
        'form': form
    }
    return render(request, 'base/tambah_penghulu.html', context)

def hapus_penghulu(request, pk):
    penghulu = Penghulu.objects.get(id=pk)
    try:
        messages.warning(request, f'Penghulu {penghulu.nama} Telah Dihapus')
        penghulu.delete()
    except:
        messages.warning(request, f'Penghulu {penghulu.nama} TIDAK DIHAPUS karena terdaftar dalam data Akad !')
        
    return redirect('penghulu')

def cetak_data(request, akad=None):
    page = "Cetak"
    html = 'cetak.html'
    now = date.today().strftime('%d %B %Y')
    print(now)
    dateMsg = f"Pekanbaru, {now}"
    if 'aksi' in request.GET:
        if request.GET['aksi'].lower() == 'cetak':
            print(request.GET['aksi'])
            html = 'cetak_data.html'  
          
    if akad != None:
        akad = Akad.objects.get(id=akad)
        pageName = 'single'
    else:
        akad = Akad.objects.filter(diperiksa=True)
        pageName = 'all'
    
    return render(request, f'base/{html}', context={'akad': akad, 'pageName': pageName, 'page':page, 'dateMsg': dateMsg})