from django.contrib import admin
from django.contrib.flatpages.admin import FlatPageAdmin
from django.contrib.flatpages.models import FlatPage
from django.utils.translation import gettext_lazy as _
from .models import Profile

admin.AdminSite.site_header = "Blog-Admin"
admin.AdminSite.site_title = "Blog Site admin"
admin.AdminSite.index_title = "Blog site adminstration"


# Define a new FlatPageAdmin
class FlatPageAdmin(FlatPageAdmin):
    fieldsets = (
        (None, {'fields': ('url', 'title', 'content', 'sites')}),
        (_('Advanced options'), {
            'classes': ('collapse',),
            'fields': (
                'enable_comments',
                'registration_required',
                'template_name',
            ),
        }),
    )

# Re-register FlatPageAdmin
admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatPageAdmin)
class ProfileAdmin(admin.ModelAdmin):
    # fields = ('user', 'Address', ('Date_Of_Birth', 'Gender'), 'profile_pic')
    list_display = ['id', '__str__', 'Gender', 'location', 'view_date_of_birth']
    list_display_links = ['__str__']
    list_per_page = 10
    list_filter = ['Gender']
    search_fields = ['id', 'user__email', 'user__username', 'user__first_name', 'user__last_name', 'location', ]
    empty_value_display = '-empty-'
    radio_fields = {"Gender": admin.HORIZONTAL}
    readonly_fields = ('Date_Of_Birth',)

    def view_date_of_birth(self, obj):
        return obj.Date_Of_Birth
    view_date_of_birth.short_description = "Date Of Birth"
    view_date_of_birth.empty_value_display = "???"

    fieldsets = (
        ('Fields', {
            'fields': ('bio', 'Address', 'location', 'profile_pic', 'Gender')
        }),
        ('More Fields', {
            'classes': ('collapse',),
            'fields': ('user', 'Date_Of_Birth'),
        }),
    )

    class Meta:
        model = Profile


admin.site.register(Profile,ProfileAdmin)
