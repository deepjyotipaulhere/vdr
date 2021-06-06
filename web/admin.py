from web.models import FileCategory, FileSubcategory, Files, User
from django.contrib import admin

# Register your models here.


class FileAdmin(admin.ModelAdmin):
    list_display = ['file', 'subcat']


admin.site.register([FileSubcategory, FileCategory, User])
admin.site.register(Files, FileAdmin)
