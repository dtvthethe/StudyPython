from django.contrib import admin

# Register your models here.
from .models import Post, Category


class PostModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'updated', 'timestamp_red_color')
    list_display_links = ['updated']
    list_filter = ('updated', 'timestamp')
    search_fields = ('title', 'updated')
    list_editable = ['title']

    class Meta:
        model = Post


class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'updated', 'timestamp')
    list_display_links = ['updated']
    list_filter = ('updated', 'timestamp')
    search_fields = ['title']
    list_editable = ['title']

    class Meta:
        model = Category


admin.site.register(Post, PostModelAdmin)
admin.site.register(Category, CategoryModelAdmin)
