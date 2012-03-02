from django.contrib import admin
from main.models import Zombie, Tweet


class ZombieAdmin(admin.ModelAdmin):
	list_display = ('name', 'cemetery',)
	search_fields = ('cemetery',)

class TweetAdmin(admin.ModelAdmin):
	list_display = ('status', 'zombie',)

admin.site.register(Zombie, ZombieAdmin)
admin.site.register(Tweet, TweetAdmin)