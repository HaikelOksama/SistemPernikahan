from django.contrib import admin
from .models import Suami, Istri, Penghulu, Akad, Wali, Profile

# Register your models here.
admin.site.register(Akad)
admin.site.register(Suami)
admin.site.register(Istri)
admin.site.register(Penghulu)
admin.site.register(Wali)
admin.site.register(Profile)