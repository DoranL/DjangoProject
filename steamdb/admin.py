from django.contrib import admin

# Register your models here.
from .models import Game

class GameAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "release_date", "price", "image")

admin.site.register(Game, GameAdmin)