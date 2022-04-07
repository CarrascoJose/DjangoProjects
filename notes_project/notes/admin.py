from django.contrib import admin
from .models import AppUser,Note

# Register your models here.
class AppUserAdmin(admin.ModelAdmin):
    list_display = ('username','email')

class NoteAdmin(admin.ModelAdmin):
    list_display = ('title','publish_date','user')

admin.site.register(AppUser,AppUserAdmin)
admin.site.register(Note,NoteAdmin)