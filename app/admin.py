from django.contrib import admin
from .models import Network
from import_export.admin import ImportExportModelAdmin
from django.db import models

@admin.register(Network)
class NetworkAdmin(ImportExportModelAdmin):
    list_display = ['governorate','area','type','speciality','provider','address','phone','discount']
    list_display_links = ['provider', 'phone','discount']
    search_fields = ['governorate','area','type','speciality','provider','address','phone','discount']
    list_filter = ['provider','governorate','area','discount']



