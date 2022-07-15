# from urllib import request
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from forms.models import Registeration
from django.utils.safestring import mark_safe
# from django.contrib.sites.shortcuts import get_current_site
from django.contrib.admin import site
import adminactions.actions as actions

# register all adminactions
actions.add_to_site(site,
                    exclude=[
                        'merge', 'export_delete_tree', 'export_as_xls',
                        'graph_queryset', 'export_as_csv', 'export_as_fixture'
                    ])


class RegAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('name', 'email', 'branch', 'phone_number', 'resume_url')
    search_fields = ('name', 'email', 'branch', 'phone_number')

    def resume_url(self, instance):
        resume = instance.resume.url
        if resume:
            return mark_safe('<a target="_blank" href="%s">Resume Link</a>' %
                             (resume))
        else:
            return '-'


admin.site.register(Registeration, RegAdmin)
