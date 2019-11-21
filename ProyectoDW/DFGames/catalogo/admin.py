from django.contrib import admin

# Register your models here.

from . models import Juego, Company, Genre, Platform

admin.site.register(Juego)
admin.site.register(Company)
admin.site.register(Genre)
admin.site.register(Platform)
