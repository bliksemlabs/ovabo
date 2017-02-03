from django.contrib import admin

from data.models import Line


class LineAdmin(admin.ModelAdmin):
    model = Line
    list_display = ('dataownercode','lineplanningnumber','publiclinenumber','headsign')
    list_filter = ('dataownercode',)

admin.site.register(Line, LineAdmin)