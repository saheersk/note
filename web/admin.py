from django.contrib import admin

from web.models import Note

class NoteAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description']

admin.site.register(Note, NoteAdmin)
