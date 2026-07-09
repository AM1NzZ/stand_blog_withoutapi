from django.contrib import admin
from  .models import Article , Category ,Comment


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','author','created_at','updated_at','published')
    list_editable = ('author','published')

admin.site.register(Article,ArticleAdmin)
admin.site.register(Category)
admin.site.register(Comment)