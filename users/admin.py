from django.contrib import admin
from .models import Profile

admin.AdminSite.site_header = "Blog-Admin"
admin.AdminSite.site_title = "Blog Site admin"
admin.AdminSite.index_title = "Blog site adminstration"
class ProfileAdmin(admin.ModelAdmin):


    #fields = ('user','Address',('Date_Of_Birth','Gender'),'profile_pic')
    list_display = ['id','__str__','Gender','location','view_Date_Of_Birth']
    list_display_links = ['__str__']
    list_per_page = 10
    list_filter = ['Gender']
    search_fields = ['id','user__email','user__username','user__first_name','user__last_name','location',]
    empty_value_display = '-empty-'
    radio_fields = {"Gender": admin.HORIZONTAL}
    readonly_fields = ('Date_Of_Birth',)
    def view_Date_Of_Birth(self,obj):
        return obj.Date_Of_Birth
    view_Date_Of_Birth.short_description = "Date Of Birth"
    view_Date_Of_Birth.empty_value_display = "???"


    fieldsets = (
        ('Fields', {
            'fields': ('bio','Address','location' ,'profile_pic', 'Gender')
        }),
        ('More Fields', {
            'classes': ('collapse',),
            'fields': ('user', 'Date_Of_Birth'),
        }),
    )

    class Meta:
        model = Profile

admin.site.register(Profile,ProfileAdmin)