from django.contrib import admin
from .models import Social

from django.utils.safestring import mark_safe
from blog_project.settings import MEDIA_URL
# Register your models here.
class SocialAdmin(admin.ModelAdmin):
    list_display = ('show_icon','title','link')
    list_editable = ('link',)

    def show_icon(self, obj):
        return mark_safe(f'<img src="/{MEDIA_URL}{obj.icon}" style="width:22px;">')
    show_icon.short_description = "Icon"
admin.site.register(Social,SocialAdmin)