from django.contrib import admin
from .models import Postblog

@admin.register(Postblog)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','status','datetime_modified')
    ordering = ('status',)
#admin.site.register(Postblog)

