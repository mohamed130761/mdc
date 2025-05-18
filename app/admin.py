from django.contrib import admin
from .models import Network,Networkeds,Networkemfa,Networkmofa,Networkexxon,Networkhorizon
from import_export.admin import ImportExportModelAdmin
from django.db import models

@admin.register(Network)
class NetworkAdmin(ImportExportModelAdmin):
    list_display = ['governorate','area','type','speciality','provider','address','phone','discount']
    list_display_links = ['provider', 'phone','discount']
    search_fields = ['governorate','area','type','speciality','provider','address','phone','discount']
    list_filter = ['provider','governorate','area','discount']




@admin.register(Networkeds)
class NetworkAdmin(ImportExportModelAdmin):
    list_display = ['governorate','area','type','speciality','provider','address','phone']
    list_display_links = ['provider', 'phone']
    search_fields = ['governorate','area','type','speciality','provider','address','phone']
    list_filter = ['provider','governorate','area']

@admin.register(Networkmofa)
class NetworkAdmin(ImportExportModelAdmin):
    list_display = ['governorate','area','type','speciality','provider','address','phone']
    list_display_links = ['provider', 'phone']
    search_fields = ['governorate','area','type','speciality','provider','address','phone']
    list_filter = ['provider','governorate','area']

@admin.register(Networkexxon)
class NetworkAdmin(ImportExportModelAdmin):
    list_display = ['governorate','area','type','speciality','provider','address','phone']
    list_display_links = ['provider', 'phone']
    search_fields = ['governorate','area','type','speciality','provider','address','phone']
    list_filter = ['provider','governorate','area']

@admin.register(Networkemfa)
class NetworkAdmin(ImportExportModelAdmin):
    list_display = ['governorate','area','type','speciality','provider','address','phone']
    list_display_links = ['provider', 'phone']
    search_fields = ['governorate','area','type','speciality','provider','address','phone']
    list_filter = ['provider','governorate','area']

@admin.register(Networkhorizon)
class NetworkAdmin(ImportExportModelAdmin):
    list_display = ['governorate','area','type','speciality','provider','address','phone']
    list_display_links = ['provider', 'phone']
    search_fields = ['governorate','area','type','speciality','provider','address','phone']
    list_filter = ['provider','governorate','area']



