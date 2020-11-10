from django.contrib import admin
from .models import Post , BlogComment , Category

# Register your models here.
admin.site.register((BlogComment,Category))


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    class Media:
        js = ('js/tinyInject.js',)