#django
from django.contrib import admin
from django.contrib.auth.models import Permission

#local
from send_sms.models import *

# Register your models here.


class DeviceAdmin(admin.ModelAdmin):
    list_display = ('user','deviceID', 'phoneNumber', 'accountEmail',)


class ContactsAdmin(admin.ModelAdmin):
    list_display = ('firstName', 'lastName', 'phoneNumber', 'user')
    # inlines = [ContactsAdminInline,]


class ContactGroupAdmin(admin.ModelAdmin):
    list_display = ('groupName',)
    list_filter = ('groupName',)
    search_fields = ('contact', 'groupName',)
    filter_horizontal = ('contact',)


admin.site.register(device, DeviceAdmin)
admin.site.register(msgTemplates, )
admin.site.register(contactgroup, ContactGroupAdmin)
admin.site.register(contacts, ContactsAdmin)
admin.site.register(Permission)
