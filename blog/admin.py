from django.contrib import admin
from .models import Post
# Register your models here.
# admin.site.register(Post)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id','title','author','date_posted','last_updated']
    list_display_links = ['title']
    list_editable = []
    list_per_page = 10
    list_filter = ['date_posted','last_updated']
    search_fields = ['id','title','content','author__email','author__username','author__first_name','author__last_name']
    date_hierarchy = 'date_posted'

    class Meta:
        model = Post
