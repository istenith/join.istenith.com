from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from results.models import ResultPage, Results
# Register your models here.


class ResultAdmin(admin.ModelAdmin):
    readonly_fields = ['default']


class ResAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['name', 'branch', 'roll_number']
    list_display = ['name', 'branch', 'roll_number']


admin.site.register(ResultPage, ResultAdmin)
admin.site.register(Results, ResAdmin)
