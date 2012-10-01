from m0m.models import *
from django.contrib import admin

class AttachmentInline(admin.TabularInline):
    model = Attachment
    #fields = ('description','file')

class EventAdmin(admin.ModelAdmin):
    list_display = ('title','date',)
    inlines = (AttachmentInline, )

admin.site.register(Event, EventAdmin)
admin.site.register(Attachment)