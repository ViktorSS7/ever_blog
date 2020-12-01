from django.contrib import admin

from .models import Post, Comment


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 2


class PostAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': [
            'title',
            'body'
        ]}),
        ('Date information', {'fields': ['date_added'], 'classes': ['collapse']}),
    ]
    inlines = [CommentInline]
    list_display = ('title', 'date_added')
    list_filter = ['date_added']
    search_fields = ['title', 'body']


class CommentAdmin(admin.ModelAdmin):
    list_filter = ['post', 'user']
    list_display = ['body', 'date_added', 'post']
    search_fields = ['body']


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
