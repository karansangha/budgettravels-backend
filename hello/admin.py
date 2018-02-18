from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import Destinations

@admin.register(Destinations)
class DestinationsAdmin(ImportExportModelAdmin):
    pass
