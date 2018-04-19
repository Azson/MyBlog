from django.contrib import admin

from .models import Post, Mood, Mark, User, MyUser, Diary
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'pub_date')

class PostAdmin1(admin.ModelAdmin):
    list_display = ('nickname', 'message', 'enabled', 'pub_time')
    ordering = ('-pub_time',)

admin.site.register(Mood)
admin.site.register(Mark, PostAdmin1)

admin.site.register(Post, PostAdmin)

admin.site.register(User)
admin.site.register(MyUser)

admin.site.register(Diary)