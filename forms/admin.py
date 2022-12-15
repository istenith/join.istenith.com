from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from forms.models import Registeration, Social_Link, Template, Terms_n_Condition, FAQ, FormPlaceholder
# from forms.models import Downloads
# from forms.models import Contact
from django.utils.safestring import mark_safe
# from django.contrib.sites.shortcuts import get_current_site
from django.contrib.admin import site
import adminactions.actions as actions
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from solo.admin import SingletonModelAdmin

# register all adminactions
actions.add_to_site(site,
                    exclude=[
                        'merge', 'export_delete_tree', 'export_as_xls',
                        'graph_queryset', 'export_as_csv', 'export_as_fixture'
                    ])


class RegAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('name', 'email', 'branch', 'phone_number',
                    'terms_confirmed')
    search_fields = ('name', 'email', 'branch', 'phone_number')

# if Resume field is required then you can go with this function otherwise for not-required field, it is not advisable to use
    # def resume_url(self, instance):
    #     resume = instance.resume.url
    #     if resume:
    #         return mark_safe('<a target="_blank" href="%s">Resume Link</a>' %
    #                          (resume))
    #     else:
    #         return '-'


class UserAdmin(ImportExportModelAdmin, UserAdmin):
    list_display = ('username', 'first_name', 'email')
    search_fields = ('email', 'first_name')


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(FAQ)
admin.site.register(FormPlaceholder, SingletonModelAdmin)
admin.site.register(Template, SingletonModelAdmin)
admin.site.register(Terms_n_Condition, SingletonModelAdmin)
admin.site.register(Social_Link)
admin.site.register(Registeration, RegAdmin)
