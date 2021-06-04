from django.contrib import admin
from api.models import person_type,person_media_type,person,person_media,person_audit

# Register your models here.

class GenericAdmin(admin.ModelAdmin):
    pass
admin.site.register(person,GenericAdmin)
admin.site.register(person_media_type,GenericAdmin)
admin.site.register(person_type,GenericAdmin)
admin.site.register(person_media,GenericAdmin)
admin.site.register(person_audit,GenericAdmin)
