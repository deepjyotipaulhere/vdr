from web.models import FileCategory, FileSubcategory, Files
from django.contrib import admin
from django.conf import settings
# Register your models here.


def custom_titled_filter(title):
    class Wrapper(admin.FieldListFilter):
        def __new__(cls, *args, **kwargs):
            instance = admin.FieldListFilter.create(*args, **kwargs)
            instance.title = title
            return instance
    return Wrapper


class FileAdmin(admin.ModelAdmin):
    list_display = ['get_cat', 'subcat', 'file','uploaded_on']
    ordering = ['-uploaded_on']
    search_fields = ['file']
    list_filter = (
        ('subcat__catName', custom_titled_filter('Category')),
        ('subcat', custom_titled_filter('Sub-category')))

    def get_cat(self, obj):
        return obj.subcat.catName

    get_cat.short_description = 'Category'
    get_cat.admin_order_field = 'subcat__catName'


admin.site.register([FileSubcategory, FileCategory])
admin.site.register(Files, FileAdmin)

admin.site.index_title = settings.PROJECT_CLIENT + " - Virtual Data Room"
admin.site.site_header = settings.PROJECT_CLIENT + " - Virtual Data Room"
