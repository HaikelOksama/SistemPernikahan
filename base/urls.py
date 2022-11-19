
from django.urls import path, include
from . import views

urlpatterns = [
    path("akad/", views.akad_view, name="akad"),
    path("akad/baru/", views.daftar_akad_view, name="daftar_akad"),
    path("akad/hapus/<int:pk>/", views.hapus_akad, name="hapus_akad"),
    path("akad/detail/<int:pk>/", views.detail_akad_view, name="detail_akad"),
    path("akad/detail/<int:pk>/wali/tambah/", views.tambah_wali, name="tambah-wali"),
    path("akad/detail/<int:akad>/wali/<int:pk>/", views.ubah_wali, name="ubah-wali"),
    path("akad/detail/<int:akad>/wali/<int:pk>/hapus/", views.hapus_wali, name="hapus-wali"),
    
    path("akad/cetak/", views.cetak_data, name="cetak-akad"),
    path("akad/cetak/<int:akad>/", views.cetak_data, name="cetak-detail"),
    
    
    path("suami/", views.data_suami_view, name="data-suami"),
    path("suami/<int:pk>/edit/", views.edit_suami_view, name="edit-suami"),
    
    path("istri/", views.data_istri_view, name="data-istri"),
    path("istri/<int:pk>/edit/", views.edit_istri_view, name="edit-istri"),
    
    path("penghulu/", views.penghulu_view, name="penghulu"),
    path("penghulu/tambah/", views.tambah_penghulu, name="tambah-penghulu"),
    path("penghulu/edit/<int:pk>/", views.ubah_penghulu, name="edit-penghulu"),
    path("penghulu/hapus/<int:pk>/", views.hapus_penghulu, name="hapus-penghulu"),
]